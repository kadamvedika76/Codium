# CodiumV1: Integrated DSA & SQL Learning Ecosystem
Codium is an interactive, full-stack learning platform designed to bridge the gap between static algorithmic coding and live technical interview mentorship. By combining a professional browser-based IDE with an sub-second Generative AI engine, Codium acts as a Socratic Tutor—analyzing your specific code variations and providing contextual logical nudges rather than spoiling the answer with direct solutions.

🚀 Core Features
Interactive Coding Workspace: Write code directly inside a rich, browser-based IDE powered by CodeMirror 6 with syntax highlighting, auto-completion, and split-screen problem/example sheets.

Contextual AI Mentor: Stuck on a problem? The "Get Hint" interface securely bundles your scratchpad code and the problem text, prompting Groq (Llama 3.1) to return 2–3 precise, conversational-filler-free logic hints tailored to your mistakes.

Adaptive Quiz Architecture: Take structured conceptual quizzes across core Data Structures (Arrays, Strings, Linked Lists, Stacks, Queues, Trees, Graphs) and database design.

Custom AI Quiz Generator: Upload specific study material or topics to dynamically parse data into custom interactive technical multiple-choice challenges.

Persistent Performance Dashboard: Track historical score records, submission verdicts (AC, WA, TLE, RE), and problem-solving analytics securely synced to your profile.

🛠️ System Architecture & Tech Stack
Codium relies on a modern Decoupled Architecture communicating over a secure, stateless REST API.

Frontend (Client-Side)
React.js (Single Page Application): Drives an instant, desktop-like user experience using client-side layout swapping (Virtual DOM Reconciliation) rather than full-browser refreshes.

CodeMirror 6: Implements an extensible syntax configuration system supporting Python, Java, and C++.

Asynchronous State Engine: Manages UI transitions natively via decoupled, background data fetching (fetch API).

Backend (Server-Side)
Django Web Framework: Houses secure endpoints, handles database relational migrations, and hosts the automated testing engine executing sandbox code metrics.

Django CORS Headers & Session Middleware: Configured with specific cross-origin controls to protect authentication session state layers between frontend (localhost:3000) and backend (localhost:8000).

AI & Infrastructure
Groq Cloud (Llama 3.1 Inference Engine): Exploits ultra-low latency LPUs (Language Processing Units) to deliver code optimization logic and hints in under 500ms.

Relational Database: Stores persistence maps of user metrics, problems, validation assertions, and historical progression tables.


🔧 Installation & Local Setup
Prerequisites
Node.js (v16+)

Python (v3.10+)

Groq API Key

