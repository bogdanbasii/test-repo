from django.urls import path
from .views import get_all_users

urlpatterns = [
    path('', get_all_users, name='user')
]
