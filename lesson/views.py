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












# class LessonListCreate(APIView):
#
#     def get(self, request, format=None):
#         lessons = Lesson.objects.all()
#         serializer = LessonSerializer(lessons, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         author = self.request.user
#         subject_id = self.request.data.get('subject_id')
#         lesson_num = self.request.data.get('lesson_num')
#         teacher_id = self.request.data.get('teacher_id')
#         duration = self.request.data.get('duration')
#         time = self.request.data.get('time')
#
#         subject = get_object_or_404(Subject, id=subject_id)
#         lesson_room = get_object_or_404(LessonRoom, id=lesson_num)
#         teacher = get_object_or_404(Teacher, id=teacher_id)
#
#         lesson = Lesson.objects.create(
#             author=author,
#             subject_id=subject,
#             lesson_num=lesson_room,
#             teach_id=teacher,
#             duration=duration,
#             time=time
#         )
#         serializer = LessonSerializer(lesson)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class LessonDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Lesson.objects.get(pk=pk)
#         except Lesson.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         lesson = self.get_object(pk)
#         serializer = LessonSerializer(lesson)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         lesson = self.get_object(pk)
#         serializer = LessonSerializer(lesson, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         lesson = self.get_object(pk)
#         lesson.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)