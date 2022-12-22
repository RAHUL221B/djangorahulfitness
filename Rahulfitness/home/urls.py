from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    
    

    path('', views.home, name='home'),
    path('home/about', views.about, name='about'),
    path(r'contact.html/', views.contact, name='contact')
    
    
]
     
    