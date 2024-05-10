# tienda/urls.py

from django.urls import path
from .views import contacto, opinion, home

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contacto, name='save_contact'),
    path('opinion/', opinion, name='save_opinion'),
]
