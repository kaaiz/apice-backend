from django.urls import path
from .views import CategoryList, CategoryDetail, ElementList, ElementDetail

urlpatterns = [
    path('element/<int:pk>/', ElementDetail.as_view()),
    path('element/', ElementList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('category/', CategoryList.as_view()),
]