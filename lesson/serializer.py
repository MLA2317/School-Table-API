from rest_framework import serializers
from .models import Subject, LessonRoom, Teacher, Lesson


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'title')


class LessonRomSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonRoom
        fields = ('id', 'room_num', 'room_type', 'capacity')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'teacher', 'first_name', 'last_name', 'subject_taught', 'level', 'teacher_img', 'created_date')


class LessonSerializer(serializers.ModelSerializer):
    subject_id = SubjectSerializer(read_only=True)
    lesson_num = LessonRomSerializer(read_only=True)
    teach_id = TeacherSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'lesson_num', 'subject_id', 'teach_id', 'duration', 'time')

