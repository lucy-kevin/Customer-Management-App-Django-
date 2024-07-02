from django.urls import path
from . import view
urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
   
]