# tienda/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('opiniones/', views.opiniones, name='opiniones'),
]
