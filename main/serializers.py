from rest_framework import serializers
from .models import Stock, Category, Equipment


class StockSerializer(serializers.ModelSerializer):
    '''Класс сериализатор для модели Stock'''
    class Meta:
        model = Stock 
        fields = '__all__'
        

class CategorySerializer(serializers.ModelSerializer):
    '''Класс сериализатор для модели Category'''
    class Meta:
        model = Category 
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    '''Класс сериализатор для модели Equipment'''
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    stock = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Equipment 
        fields = '__all__'