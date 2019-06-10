from rest_framework import serializers
from .models import Element, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'text', 'image', 'created_date',)
        model = Category

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'text', 'image', 'category', 'display', 'created_date',)
        model = Element