from django.contrib import admin
from .models import Subject, LessonRoom, Lesson, Teacher

admin.site.register(Subject),
admin.site.register(LessonRoom),
admin.site.register(Lesson),
admin.site.register(Teacher)
