from rest_framework import serializers
from .models import Element, Category, Type, Product
from django.contrib.auth.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField()
    #first_name = serializers.CharField(required=False, default='')
    #last_name = serializers.CharField(required=False, default='')
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('username', 'password', 'email', 'first_name', 'last_name',) # there what you want to initial.

    def create(self, validated_data):
        user = User.objects.create(
            username= validated_data['username'],
            email = validated_data['email'],
            #first_name = validated_data['first_name'],
            #last_name = validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active',)
        #fields = ('__all__')
        exclude = ('password', 'user_permissions', 'groups', 'date_joined', 'is_superuser',)

class PasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password', 'confirm_password')

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