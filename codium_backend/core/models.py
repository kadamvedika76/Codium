from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# 1. USER PROFILE
# Extends the built-in Django User to track points and progress
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    points = models.IntegerField(default=0)
    solved_problems = models.ManyToManyField('Problem', blank=True, related_name='solvers')

    def __str__(self):
        return f"{self.user.username}'s Profile"


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# 2. CODING PROBLEMS
class Problem(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()  # The actual problem statement
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    sample_input = models.TextField()
    sample_output = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_problems')
    topic = models.CharField(max_length=50, default='Arrays')

    def __str__(self):
        return self.title


# 3. TEST CASES
# Hidden data used to validate user code
class TestCase(models.Model):
    problem = models.ForeignKey(Problem, related_name='testcases', on_delete=models.CASCADE)
    input_data = models.TextField()
    expected_output = models.TextField()

    def __str__(self):
        return f"Testcase for {self.problem.title}"


# 4. CONTESTS
# Groups problems together for a specific timeframe
class Contest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    problems = models.ManyToManyField(Problem, related_name='contests')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_contests')
    participants = models.ManyToManyField(User, related_name='joined_contests', blank=True)

    def __str__(self):
        return self.title

    @property
    def is_active(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time


# 5. SUBMISSIONS
# Records every attempt a user makes on a problem
class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.SET_NULL, null=True, blank=True)
    code = models.TextField()
    language = models.CharField(max_length=20) # e.g., 'python', 'java', 'c'
    status = models.CharField(max_length=20, default='Pending') # Accepted, WA, TLE, RE
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} ({self.status})"


# 6. QUIZ SYSTEM
# For tech MCQs practice
class QuizQuestion(models.Model):
    question_text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1) # Stores 'A', 'B', 'C', or 'D'
    topic = models.CharField(max_length=100) # e.g., 'DBMS', 'OS', 'Python'

    def __str__(self):
        return f"{self.topic}: {self.question_text[:50]}..."


class CustomQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='quizzes/pdfs/')
    topic_name = models.CharField(max_length=255)
    generated_questions = models.JSONField() # Stores the list of Qs, Options, and Answers
    created_at = models.DateTimeField(auto_now_add=True)

class TopicContent(models.Model):
    CATEGORY_CHOICES = [('dsa', 'DSA'), ('sql', 'SQL')]
    topic_name = models.CharField(max_length=100) # e.g., 'Strings'
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    content_data = models.JSONField() # Stores the entire structure: description, sections, examples

    def __str__(self):
        return f"{self.category.upper()} - {self.topic_name}"
    
class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_results')
    score = models.IntegerField()
    total_questions = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}/{self.total_questions}"