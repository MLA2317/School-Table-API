from django.contrib import admin
from .models import Subject, LessonRoom, Lesson, Teacher

admin.site.register(Subject),
admin.site.register(LessonRoom),
admin.site.register(Lesson),


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'subject_taught', 'level', 'teacher_img', 'created_date')
