from rest_framework import generics, permissions

from .models import Stock, Category, Equipment
from .serializers import StockSerializer, CategorySerializer, EquipmentSerializer


class EquipmentDetailViewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        elif request.user.is_staff:
            return True
        return False


class StockView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated,]


class StockDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class  = StockSerializer
    queryset = Stock.objects.all()
    permission_classes = [EquipmentDetailViewPermission,]


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated,]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class  = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [EquipmentDetailViewPermission,]


class EquipmentView(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated,]


class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class  = EquipmentSerializer
    queryset = Equipment.objects.all()
    permission_classes = [EquipmentDetailViewPermission,]
