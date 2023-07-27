from rest_framework import serializers
from .models import Student, Group


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'student', 'first_name', 'last_name', 'date_of_birth', 'student_image', 'group', 'is_have', 'created_date')


class GroupSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ('id', 'title', 'students', 'student_count')

    def get_student_count(self, obj):
        return obj.students.count()


