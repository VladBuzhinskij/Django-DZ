from django.contrib import admin
from django.urls import path,include
from DZ2 import views

app_name="DZ2"
urlpatterns = [
    path('',views.orders, name='order'),
    path('orders',views.orders, name='orders'),
]