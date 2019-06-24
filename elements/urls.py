from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name="login"),
    path('change-password/', views.ChangePassword.as_view(), name="change-password"),
    path('register/', views.Register.as_view(), name="register"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('element/<int:pk>/', views.ElementDetail.as_view()),
    path('element/', views.ElementList.as_view()),
    path('type/<int:pk>/', views.TypeDetail.as_view()),
    path('type/', views.TypeList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('product/', views.ProductList.as_view()),
]