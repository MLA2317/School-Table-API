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
    teach_id = serializers.SlugRelatedField(read_only=True, slug_field='first_name')#bu teacher_id ichidan faqat ismini oladi qolgan malumotlari chiqmidi

    class Meta:
        model = Lesson
        fields = ('id', 'lesson_num', 'subject_id', 'teach_id', 'duration', 'time')


class TableItemGETSerializer(serializers.ModelSerializer):
    group = SimpleGroupSerializer(read_only=True)
    lesson = SimpleLessonSerializer(read_only=True)
    week = WeekSerializer(read_only=True)

    class Meta:
        model = TableItem
        fields = ('id', 'shift', 'week', 'group', 'lesson', 'time')


class TableItemPOSTSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    lesson = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all())
    week = serializers.PrimaryKeyRelatedField(queryset=Week.objects.all())

    class Meta:
        model = TableItem
        fields = ('id', 'shift', 'week', 'group', 'lesson', 'time')


class TableGETSerializer(serializers.ModelSerializer):
    table_id = TableItemGETSerializer(read_only=True)

    class Meta:
        model = Table
        fields = ('id', 'table_id', 'created_date')


class TablePOSTSerializer(serializers.ModelSerializer):
    table_id = serializers.PrimaryKeyRelatedField(queryset=TableItem.objects.all())

    class Meta:
        model = Table
        fields = ('id', 'table_id', 'created_date')


