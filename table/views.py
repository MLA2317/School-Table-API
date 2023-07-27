from django.shortcuts import render, get_object_or_404
from .serializer import WeekSerializer, TableItemPOSTSerializer, TableItemGETSerializer
from .models import Week, TableItem, Table
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class WeekListCreate(generics.ListCreateAPIView):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer


class TableItemListApiView(generics.ListAPIView):
    queryset = TableItem.objects.all()
    serializer_class = TableItemGETSerializer


class TableItemCreateApiView(generics.CreateAPIView):
    queryset = TableItem.objects.all()
    serializer_class = TableItemPOSTSerializer

    # def get_queryset(self):
    #     table_item = TableItem.objects.all()
    #     return table_item
    #
    # def get(self, request, *args, **kwargs):
    #     try:
    #         table_item_id = request.query_params["id"]
    #         if table_item_id != None:
    #             table_item = TableItem.objects.get(id=table_item_id)
    #             serializer = TableItemSerializer(table_item)
    #     except:
    #         table_item = self.get_queryset()
    #         serializer = TableItemSerializer(table_item, many=True)
    #
    #     return Response(serializer.data)



