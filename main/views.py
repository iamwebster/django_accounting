from rest_framework import generics 

from .models import Stock, Category, Equipment
from .serializers import StockSerializer, CategorySerializer, EquipmentSerializer


class StockView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class  = StockSerializer
    queryset = Stock.objects.all()


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class  = CategorySerializer
    queryset = Category.objects.all()


class EquipmentView(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class  = EquipmentSerializer
    queryset = Equipment.objects.all()

