from django.urls import path
from .views import WeekListCreate, TableItemCreateApiView, TableItemListApiView


urlpatterns = [
    path('week/list-create/', WeekListCreate.as_view()),
    path('tableitems/list/', TableItemListApiView.as_view(), name='tableitem_list'),
    path('tableitems/create/', TableItemCreateApiView.as_view(), name='tableitem_create'),

]