from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Profile # Import your Profile model
from .models import Problem,TestCase
from .models import QuizResult

import os
import json
from dotenv import load_dotenv # Import this
from groq import Groq
# ... other imports ...

# Load the .env file
load_dotenv()

# Initialize Groq using the environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email', '')

            # 1. Check if user already exists BEFORE trying to create
            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "This username is already taken."}, status=400)

            # 2. Create the user
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            
            # 3. Safe Profile Creation (Handles signals gracefully)
            Profile.objects.get_or_create(user=user)
            
            # 4. Log them in to the session
            login(request, user)
            
            # 5. Return the 'user' object inside the response
            return JsonResponse({
                "message": "User created",
                "username": user.username,
                "email": user.email
            }, status=201)

        except Exception as e:
            # If we get here, something actually failed
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return JsonResponse({
                    "message": "Logged in", 
                    "username": user.username,
                    "email": user.email
                })
            return JsonResponse({"error": "Invalid credentials"}, status=401)
        except Exception as e:
            print(e)
            return JsonResponse({"error": "Internal server error"}, status=500)

def get_problems(request):
    """Returns all problems for the Practice pages"""
    # We use .values() to convert database objects into a JSON-friendly format
    problems = list(Problem.objects.values(
        'id', 'title', 'description', 'difficulty', 
        'topic', 'sample_input', 'sample_output'
    ))
    return JsonResponse(problems, safe=False)

@csrf_exempt
def add_problem_with_testcases(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            #creating problem

            problem=Problem.objects.create(
                title=data['title'],
                description=data['description'],
                difficulty=data['difficulty'],
                sample_input=data.get('sample_input',''),
                sample_output=data.get('sample_output',''),
                created_by=request.user if request.user.is_authenticated else None
            )

            #creating hidden testcases
            testcases_data = data.get('testcases',[])
            for tc in testcases_data:
                TestCase.objects.create(
                    problem=problem,
                    input_data=tc['input'],
                    expected_output=tc['output']
                )
            return JsonResponse({"message":"Problem and Test Cases saved!","id":problem.id},status=201)
        except Exception as e:
            return JsonResponse({"error",str(e)},status=400)
        
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Submission, QuizQuestion # Assuming you track quiz results

@login_required
def get_user_stats(request):
    user = request.user
    profile = user.profile
    
    # Count unique problems solved
    solved_count = Submission.objects.filter(user=user, status='AC').values('problem').distinct().count()
    
    # 🌟 UPDATED: Count quizzes from the database
    quiz_count = QuizResult.objects.filter(user=user).count()
    
    data = {
        "username": user.username,
        "email": user.email,
        "points": profile.points,
        "solved_count": solved_count,
        "quiz_count": quiz_count,
        "bio": profile.bio
    }
    return JsonResponse(data)
        

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Problem, TestCase, Submission, Profile
from .utils.executor import evaluate_submission

@csrf_exempt
def submit_code(request):
    if request.method=="POST":
        try:
            data = json.loads(request.body)
            user=request.user
            problem_id=data.get('problem_id')
            user_code=data.get('code')
            language=data.get('language').lower()

            #fetching testcases from models
            problem=Problem.objects.get(id=problem_id)
            test_cases_query=TestCase.objects.filter(problem=problem)

            formatted_test_cases=[
                {"input":tc.input_data, "output":tc.expected_output}
                for tc in test_cases_query
            ]

            result=evaluate_submission(user_code,language,formatted_test_cases)

            submission=Submission.objects.create(
                user=user,
                problem=problem,
                code=user_code,
                language=language,
                status=result['verdict']
            )

            if result['verdict']=='AC':
                profile=user.profile
                if not profile.solved_problems.filter(id=problem.id).exists():
                    points_map={'Easy':10,'Medium':30,'Hard':50}
                    earned_points=points_map.get(problem.difficulty,10)
                    profile.points+=earned_points
                    profile.solved_problems.add(problem)
                    profile.save()
                    result['message']=f'Success! You earned {earned_points} points.'
                else:
                    result['message']='Accepted! (Points already awarded)'
            return JsonResponse(result)
        # In your views.py inside submit_code
        except Exception as e:
            # We change 'verdict' to 'status' to match what the frontend expects
            return JsonResponse({
                "status": "error", 
                "verdict": "Error",
                "message": "A system or syntax error occurred.",
                "output": str(e) # This sends the actual Traceback/SyntaxError to the frontend
            }, status=200) # Keep 200 so the frontend catch block doesn't trigger
        
import json
import fitz  # PyMuPDF
from groq import Groq
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomQuiz

# Initialize Groq Client

import json
import fitz  # PyMuPDF
from groq import Groq
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomQuiz

# Replace with your actual key

@csrf_exempt
def generate_quiz_from_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf'):
        pdf_file = request.FILES['pdf']
        
        # 1. Parse and Validate Question Count
        try:
            total_requested = int(request.POST.get('count', 5))
            total_requested = min(max(total_requested, 1), 100)
        except (ValueError, TypeError):
            total_requested = 5
        
        # 2. Extract Text from PDF
        text = ""
        try:
            # Read PDF from memory
            pdf_stream = pdf_file.read()
            with fitz.open(stream=pdf_stream, filetype="pdf") as doc:
                # Extract first 15,000 characters to stay within context limits
                for page in doc:
                    text += page.get_text()
                    if len(text) > 15000:
                        break
        except Exception as e:
            return JsonResponse({"error": f"PDF Read Error: {str(e)}"}, status=400)

        # 3. Chunked Generation Loop
        all_questions = []
        batch_size = 20  # Batch size to prevent output token cut-offs
        
        try:
            while len(all_questions) < total_requested:
                remaining = total_requested - len(all_questions)
                current_batch_count = min(batch_size, remaining)

                completion = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "system", 
                            "content": "You are a quiz generator. Return ONLY a JSON object with a key 'questions' containing a list of objects. No intro text."
                        },
                        {
                            "role": "user", 
                            "content": f"""
                                Generate {current_batch_count} unique MCQs from the text.
                                Format: {{"questions": [ {{"question": "...", "options": ["...", "...", "...", "..."], "answer": "..."}} ]}}
                                
                                TEXT: {text[:12000]}
                            """
                        }
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.7,
                )

                # 4. Robust JSON Parsing
                raw_content = completion.choices[0].message.content
                
                # Strip potential markdown backticks AI might add
                clean_content = raw_content.replace('```json', '').replace('```', '').strip()
                
                try:
                    response_data = json.loads(clean_content)
                except json.JSONDecodeError:
                    continue # Try the loop again if AI sent malformed JSON

                # 5. Handle List vs Dict (The Fix for your error)
                batch_list = []
                if isinstance(response_data, dict):
                    # Try to get the list from the 'questions' key
                    batch_list = response_data.get('questions', [])
                elif isinstance(response_data, list):
                    # If the AI ignored JSON mode and sent a raw list
                    batch_list = response_data

                if batch_list:
                    all_questions.extend(batch_list)
                
                # Stop if the AI stops generating or we hit the limit
                if not batch_list or len(all_questions) >= total_requested:
                    break

            # 6. Save to Database for History
            final_questions = all_questions[:total_requested]
            if request.user.is_authenticated:
                CustomQuiz.objects.create(
                    user=request.user,
                    pdf_file=pdf_file,
                    topic_name=pdf_file.name,
                    generated_questions=final_questions
                )

            # 7. Return exactly what the React frontend expects
            return JsonResponse({"questions": final_questions})

        except Exception as e:
            print(f"Server-side Error: {e}")
            return JsonResponse({"error": f"AI Generation Error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request. Please upload a PDF."}, status=400)

from django.http import JsonResponse
from .models import QuizQuestion

def get_quiz_questions(request):
    # Get the 'topic' from the URL: /api/quiz/questions/?topic=Strings
    topic = request.GET.get('topic')
    
    if topic:
        # Filter questions by topic
        questions_query = QuizQuestion.objects.filter(topic=topic)
        
        # Convert QuerySet to a list of dictionaries for JSON
        questions_list = []
        for q in questions_query:
            questions_list.append({
                "id": q.id,
                "question": q.question_text,
                "options": [q.option_a, q.option_b, q.option_c, q.option_d],
                "correct_answer": q.correct_answer,
                "topic": q.topic
            })
        
        return JsonResponse(questions_list, safe=False)
    
    return JsonResponse({"error": "Topic parameter is required"}, status=400)

from django.http import JsonResponse
from .models import TopicContent

def get_topic_content(request, category):
    topic = request.GET.get('topic')
    
    # We use __iexact to make sure "Basics" matches "basics" safely
    content = TopicContent.objects.filter(
        topic_name__iexact=topic, 
        category=category
    ).first()
    
    if content:
        return JsonResponse(content.content_data)
    
    # Improved error message for easier debugging in your browser console
    return JsonResponse({
        "error": f"Content not found for topic: '{topic}' in category: '{category}'"
    }, status=404)


@csrf_exempt
def submit_quiz(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user = request.user
            score = data.get('score')
            total = data.get('total')

            # 1. Save the Quiz Result
            QuizResult.objects.create(
                user=user,
                score=score,
                total_questions=total
            )

            # 2. Award Points (e.g., 5 points per correct answer)
            profile = user.profile
            points_earned = score * 1
            profile.points += points_earned
            profile.save()

            return JsonResponse({
                "status": "success",
                "message": f"Quiz submitted! You earned {points_earned} points.",
                "points": profile.points
            })
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
        
@csrf_exempt  # Use @login_required in production for security
def get_problem_hint(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            title = data.get('problem_title')
            description = data.get('problem_description')
            user_code = data.get('user_code')
            language = data.get('language')

            # Prompt Engineering: We want a mentor, not a solution provider
            # Inside your get_problem_hint view
            prompt = f"""
            Problem: {title}
            Description: {description}
            User Code: {user_code}

            Provide exactly 3 short bullet-point hints for the user. 
            Rules:
            - No introductory text (like "Here are your hints").
            - No closing text (like "Hope this helps").
            - Max 2 sentences per hint.
            - Focus on logic and edge cases.
            """

            completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="openai/gpt-oss-120b",
                temperature=0.5, # Lower temperature makes the AI more concise and focused
            )

            hints = completion.choices[0].message.content
            return JsonResponse({"hints": hints})

        except Exception as e:
            print(f"ERROR IN GET_HINT: {str(e)}") # This will show up in your Django terminal
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)