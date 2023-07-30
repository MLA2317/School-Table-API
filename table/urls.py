from django.urls import path, include
from .views import WeekListCreate, TableItemCreateApiView, TableItemListApiView, TableItemRUDApiView, \
    TableList, TableCreate, TableRUD


urlpatterns = [
    path('week/list-create/', WeekListCreate.as_view()),

    path('tableitems/list/', TableItemListApiView.as_view()),
    path('tableitems/create/', TableItemCreateApiView.as_view()),
    path('tableitems/rud/<int:pk>/', TableItemRUDApiView.as_view()),

    path('table/list/', TableList.as_view()),
    path('table/create/', TableCreate.as_view()),
    path('table/rud/<int:pk>/', TableRUD.as_view()),

    path('', include('table.mvt.urls', namespace='mvt'))
]