from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_purchases, name='get_all_purchases'),
]