import subprocess
import tempfile
import os
import time
import sys
import glob
import logging
import gc



logger = logging.getLogger(__name__)

def is_safe(code):
    # Keywords that are strictly forbidden
    forbidden = [
        'os.', 'sys.', 'subprocess', 'open', 'write', 'executable', 
        'shutil', 'socket', 'eval', 'exec', '__import__', 'getattr',
        'rmdir', 'remove', 'unlink', 'pathlib'
    ]
    
    for word in forbidden:
        if word in code:
            return False, f"Use of '{word}' is not allowed for security reasons."
    return True, None

def clean_output(text):
    return text.strip()

def run_python(code, input_data):
    filename = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
            f.write(code.encode())
            filename = f.name

        start = time.time()
        result = subprocess.run(
            [sys.executable, filename],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=2
        )
        runtime = (time.time() - start) * 1000

        if result.returncode != 0:
            return "RE", result.stderr, runtime

        return result.stdout.strip(), result.stderr, runtime

    except subprocess.TimeoutExpired:
        return "TLE", None, 2000

    except FileNotFoundError:
        return "RE", "Python interpreter not found on server", 0

    finally:
        if filename and os.path.exists(filename):
            os.remove(filename)

def run_c(code, input_data):
    c_file = None
    exe_file = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".c") as f:
            f.write(code.encode())
            c_file = f.name

        exe_file = c_file[:-2] + ".exe"

        compile_process = subprocess.run(
            ["gcc", c_file, "-o", exe_file],
            capture_output=True,
            text=True
        )

        if compile_process.returncode != 0:
            return "CE", compile_process.stderr, 0

        start = time.time()
        print(f"DEBUG: Executing code with STDIN: {repr(formatted_input)}")
        run_process = subprocess.run(
            [exe_file],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=2
        )
        runtime = (time.time() - start) * 1000

        if run_process.returncode != 0:
            return "RE", run_process.stderr, runtime

        return run_process.stdout.strip(), run_process.stderr, runtime

    except subprocess.TimeoutExpired:
        return "TLE", None, 2000

    except FileNotFoundError:
        return "CE", "GCC compiler not found on server", 0

    finally:
    # force garbage collection first
    
        gc.collect()
        if c_file and os.path.exists(c_file):
            try:
                os.remove(c_file)
            except Exception as e:
                logger.warning(f"Could not delete c file: {e}")
        
        if exe_file and os.path.exists(exe_file):
            if os.name == 'nt':
                # Windows specific fix
                import ctypes
                for attempt in range(10):  # try 10 times
                    try:
                        os.remove(exe_file)
                        logger.debug(f"Deleted exe on attempt {attempt + 1}")
                        break
                    except PermissionError:
                        time.sleep(0.2)  # wait longer — 200ms
                else:
                    # rename instead of delete
                    # renamed files dont cause conflicts
                    try:
                        trash_name = exe_file + ".old"
                        os.rename(exe_file, trash_name)
                        logger.warning(f"Renamed locked file to {trash_name}")
                    except Exception as e:
                        logger.warning(f"Could not delete or rename: {e}")
            else:
                os.remove(exe_file)

def run_java(code, input_data):
    try:
        with open("Main.java", "w") as f:
            f.write(code)

        compile_process = subprocess.run(
            ["javac", "Main.java"],
            capture_output=True,
            text=True
        )

        if compile_process.returncode != 0:
            return "CE", compile_process.stderr, 0

        start = time.time()
        run_process = subprocess.run(
            ["java", "Main"],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=2
        )
        runtime = (time.time() - start) * 1000

        if run_process.returncode != 0:
            return "RE", run_process.stderr, runtime

        return run_process.stdout.strip(), run_process.stderr, runtime

    except subprocess.TimeoutExpired:
        return "TLE", None, 2000

    except FileNotFoundError:
        return "CE", "Java compiler not found on server", 0


    finally:
        if os.path.exists("Main.java"): 
            os.remove("Main.java")
        for class_file in glob.glob("*.class"):
            os.remove(class_file)
def evaluate_submission(code, language, test_cases):

    safe, message = is_safe(code)
    if not safe:
        return {"verdict": "Security Error", "message": message}

    # validation checks
    if not code or not code.strip():
        return {"verdict": "Error", "message": "No code submitted"}
    
    if language not in ["python", "c", "java"]:
        return {"verdict": "Error", "message": f"Unsupported language: {language}"}
    
    if not test_cases or len(test_cases) == 0:
        return {"verdict": "Error", "message": "No test cases found"}

    total_runtime = 0

    for i, case in enumerate(test_cases, start=1):
        input_data = case["input"]
        expected_output = case["output"]

        if language == "python":
            output, error, runtime = run_python(code, input_data)
        elif language == "c":
            output, error, runtime = run_c(code, input_data)
        elif language == "java":
            output, error, runtime = run_java(code, input_data)

        total_runtime += runtime

        if output == "TLE":
            logger.warning(f"Test Case {i} → TLE")
            return {"verdict": "TLE", "test_case": i, "time_ms": 2000}

        if output == "CE":
            logger.error(f"Compilation Error: {error}")
            return {"verdict": "CE", "error": error, "test_case": i}

        if output == "RE":
            logger.error(f"Test Case {i} → Runtime Error: {error}")
            return {"verdict": "RE", "error": error, "test_case": i}

        if clean_output(output) == clean_output(expected_output):
            logger.info(f"Test Case {i} → PASS ({runtime:.1f}ms)")
        else:
            logger.warning(f"Test Case {i} → WA")
            return {
                "verdict": "WA",
                "test_case": i,
                "expected": expected_output,
                "got": output,
                "time_ms": round(runtime, 2)
            }

    return {"verdict": "AC", "time_ms": round(total_runtime, 2)}