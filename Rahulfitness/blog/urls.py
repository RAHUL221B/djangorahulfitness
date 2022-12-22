from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
   
    path('', views.home, name='home'),
    path(r'allaboutabs.html/', views.All_about_Abs, name='all about abs'),
    path('blog/fat_loss/', views.fat_loss, name='fat loss'),
    path('<str:slug>', views.Nutrition, name='Nutrition'),
    path('<str:slug>', views.Supplements, name='Supplements'),
    path('<str:slug>', views.Training, name='Training'),
  
]