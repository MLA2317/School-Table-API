from django.shortcuts import render, get_object_or_404
from .serializer import WeekSerializer, TableItemPOSTSerializer, TableItemGETSerializer, TableGETSerializer, TablePOSTSerializer
from .models import Week, TableItem, Table
from rest_framework import generics, permissions, status, views
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


class TableItemRUDApiView(views.APIView):
    queryset = TableItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        instance = TableItem.objects.get(id=pk)
        serializer = TableItemGETSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        instance = TableItem.objects.get(id=pk)
        serializer = TableItemPOSTSerializer(data=data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        instance = TableItem.objects.get(id=pk)
        instance.delete()
        return Response({"detail": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)


class TableList(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableGETSerializer


class TableCreate(generics.CreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TablePOSTSerializer


class TableRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TablePOSTSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]

