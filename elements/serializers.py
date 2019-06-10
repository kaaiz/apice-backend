from rest_framework import serializers
from .models import Element, Category, Type, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'text', 'image', 'created_date',)
        model = Category

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'text', 'image', 'category', 'display', 'created_date',)
        model = Element

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'text', 'image', 'created_date',)
        model = Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'text', 'image', 'category', 'display', 'price', 'stock', 'created_date',)
        model = Element