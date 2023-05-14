from django.urls import path, include
from .views import UserViewSet
from rest_framework import SimpleRouter

router = SimpleRouter()
router.register('', UserViewSet, basename='users')

urlpatterns = [
    # path('userlist/', UserListView.as_view(), name='user_list'),
    # path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    # path('create_user/', UserCreateView.as_view(), name='user_create'),
    # path('', include(router.urls)),
]

urlpatterns += router.urls
