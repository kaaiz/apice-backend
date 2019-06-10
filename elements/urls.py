from django.urls import path
from .views import CategoryList, CategoryDetail, ElementList, ElementDetail, TypeList, TypeDetail, ProductList, ProductDetail

urlpatterns = [
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('category/', CategoryList.as_view()),
    path('element/<int:pk>/', ElementDetail.as_view()),
    path('element/', ElementList.as_view()),
    path('type/<int:pk>/', TypeDetail.as_view()),
    path('type/', TypeList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('product/', ProductList.as_view()),
]