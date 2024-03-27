from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import Table, Meal, Order
from apps.serializers import TableModelSerializer, MealModelSerializer, OrderModelSerializer, OrderDetailModelSerializer


# Create your views here.
class TableListAPIView(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableModelSerializer

    @swagger_auto_schema(tags=['cafe'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class TypeAPIView(APIView):
    @swagger_auto_schema(tags=['cafe'])
    def get(self, request, *args, **kwargs):
        types = []
        for i in Meal.Type.choices:
            types.append(i)
        return Response(types)


class MealListAPIView(generics.ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']

    @swagger_auto_schema(tags=['cafe'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer

    @swagger_auto_schema(tags=['cafe'])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class OrderRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailModelSerializer
