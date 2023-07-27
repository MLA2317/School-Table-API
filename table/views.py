from django.shortcuts import render
from .serializer import WeekSerializer, TableItemSerializer
from .models import Week, TableItem, Table
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class WeekListCreate(generics.ListCreateAPIView):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer


class TableItemListCreate(APIView):

    def get(self, request):
        table_items = TableItem.objects.all()
        serializer = TableItemSerializer(table_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TableItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
