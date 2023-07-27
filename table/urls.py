from django.urls import path
from .views import WeekListCreate, TableItemListCreate


urlpatterns = [
    path('week/list-create/', WeekListCreate.as_view()),
    path('tableitems/list-create/', TableItemListCreate.as_view(), name='tableitem_list_create'),
]