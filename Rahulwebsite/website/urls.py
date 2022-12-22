
from django.urls import path
from . import views
from . views import Addpostview, Updatepostview, Deletepostview, Addcategoryview, CategoryView
from . views import fatloss
from . views import fatlossPost


urlpatterns = [

path('', views.home, name="home"),
path('Nutrition', views.Nutrition, name="Nutrition"),
path('supplements', views.supplements, name="supplements"),
path('Training', views.Training, name="Training"),
path('Allaboutabs', views.Allaboutabs, name="Allaboutabs"),
path('contact.html', views.contact, name="contact"),
# path('fatloss.html', views.fatloss, name="fatloss"),
path('fatloss.html',fatloss.as_view(), name="fatloss"),
path('calcount.html', views.calcount, name="calcount"),
# path('fatlossPost/<str:slug>',views.fatlossPost,name ='fatlossPost'),
path('fatlossPost/<int:pk>', fatlossPost.as_view(),name ='fatlossPost'),
# path('fatlossPost.html',views.fatlossPost,name ='fatlossPost'),
path('search',views.search,name = 'search'),
# path('addpost/',views.Addpostview,name = 'addpost'),
path('addpost/',Addpostview.as_view(),name = 'addpost'),
path('addcategory/',Addcategoryview.as_view(),name = 'addcategory'),
path('fatlossPost/edit/<int:pk>',Updatepostview.as_view(),name = 'updatepost'),
path('fatlossPost/<int:pk>/remove',Deletepostview.as_view(),name = 'deletepost'),
path('<str:cats>/',views.CategoryView,name = 'category'),

]
