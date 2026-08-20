from django.contrib import admin
from .models import Profile, Problem, TestCase, Contest, Submission, QuizQuestion

# Register your models here so they show up in /admin/
admin.site.register(Profile)
admin.site.register(Problem)
admin.site.register(TestCase)
admin.site.register(Contest)
admin.site.register(Submission)
admin.site.register(QuizQuestion)