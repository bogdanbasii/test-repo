from django.urls import path, include
from .views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    # path('userlist/', UserListView.as_view(), name='user_list'),
    # path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    # path('create_user/', UserCreateView.as_view(), name='user_create'),
    path('', include(router.urls)),
]

