from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import SubjectSerializer, LessonRomSerializer, TeacherSerializer, LessonSerializer
from .models import Subject, LessonRoom, Lesson, Teacher


class SubjectListCreate(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = 'pk'


class LessonRoomListCreate(generics.ListCreateAPIView):
    queryset = LessonRoom.objects.all()
    serializer_class = LessonRomSerializer


class LessonRoomRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = LessonRoom.objects.all()
    serializer_class = LessonRomSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]


class TeacherListCreate(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'pk'


class LessonListCreate(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = 'pk'

