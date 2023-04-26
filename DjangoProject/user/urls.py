from django.urls import path
from .views import UserListView, UserDetailView, UserCreateView

urlpatterns = [
    path('userlist/', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('create_user/', UserCreateView.as_view(), name='user_create'),
]
