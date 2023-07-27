from django.urls import path
from .views import StudentCreateList, GroupListCreate, StudentRUD, GroupRUD


urlpatterns = [
    path('stud/list-create/', StudentCreateList.as_view()),
    path('stud/rud/<int:pk>/', StudentRUD.as_view()),
    path('gr/list-create/', GroupListCreate.as_view()),
    path('gr/rud/<int:pk>/', GroupRUD.as_view())
]
