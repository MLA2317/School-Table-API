from django.urls import path
from .view import index

app_name = 'mvt'

urlpatterns = [
    path('index/', index, name='index')
]
