from django.contrib import admin
from .models import Question
from .models import Choice
from .models import Submission
from .models import Lesson
from .models import Enrollment
from .models import Course
from .models import User

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionInline(admin.TabularInline):
    model = Question

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Submission)
admin.site.register(Enrollment)
admin.site.register(Course)
admin.site.register(User)
