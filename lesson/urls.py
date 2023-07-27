from django.urls import path
from .views import SubjectListCreate, SubjectRUD, LessonRoomListCreate, LessonRoomRUD, TeacherListCreate, TeacherRUD, \
    LessonListCreate, LessonRUD


urlpatterns = [
    path('sub/list/create/', SubjectListCreate.as_view()),
    path('sub/rud/<int:pk>/', SubjectRUD.as_view()),

    path('les/room/list/create/', LessonRoomListCreate.as_view()),
    path('les/room/rud/<int:pk>/', LessonRoomRUD.as_view()),

    path('teacher/list/create/', TeacherListCreate.as_view()),
    path('teacher/rud/<int:pk>/', TeacherRUD.as_view()),

    path('les/list/create/', LessonListCreate.as_view()),
    path('les/detail/<int:pk>/', LessonRUD.as_view()),

    # path('les/list/create/', LessonListCreate.as_view()),
    # path('les/rud/<int:pk>/', LessonRUD.as_view())
]
