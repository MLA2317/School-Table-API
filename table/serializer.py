from rest_framework import serializers
from .models import Table, TableItem, Week
from group.models import Group
from lesson.models import Lesson
from group.serializer import GroupSerializer
from lesson.serializer import SubjectSerializer, LessonRomSerializer
from lesson.serializer import LessonSerializer


class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = ('id', 'title')


class SimpleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title')


class SimpleLessonSerializer(serializers.ModelSerializer):
    subject_id = SubjectSerializer(read_only=True)
    lesson_num = LessonRomSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'lesson_num', 'subject_id', 'teach_id', 'duration', 'time')


class TableItemSerializer(serializers.ModelSerializer):
    group = SimpleGroupSerializer(read_only=True)
    lesson = SimpleLessonSerializer(read_only=True)
    week = WeekSerializer(read_only=True)

    class Meta:
        model = TableItem
        fields = ('id', 'shift', 'week', 'group', 'lesson', 'time')

