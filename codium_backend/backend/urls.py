from django.contrib import admin
from django.urls import path
from core.views import signup_view, login_view,add_problem_with_testcases,get_user_stats,get_problems,submit_code, generate_quiz_from_pdf,get_quiz_questions,get_topic_content
from core.views import submit_quiz,get_problem_hint # Import your views from core


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # These match your React fetch('http://localhost:8000/api/...')
    path('api/signup/', signup_view, name='signup'),
    path('api/login/', login_view, name='login'),
    path('api/add-problem/',add_problem_with_testcases,name='add_problems'),
    path('api/problems/', get_problems, name='get_problems'),
    path('api/user/stats/', get_user_stats, name='user_stats'),
    path('api/code/submit/', submit_code, name='submit_code'),
    path('api/generate-quiz/', generate_quiz_from_pdf, name='generate_quiz_from_pdf'),
    path('api/quiz/questions/', get_quiz_questions, name='get_quiz_questions'),
    path('api/learn/<str:category>/', get_topic_content, name='get_topic_content'),
    path('api/quiz/submit/', submit_quiz, name='submit_quiz'),
    path('api/problems/get-hint/', get_problem_hint, name='get_problem_hint')

]