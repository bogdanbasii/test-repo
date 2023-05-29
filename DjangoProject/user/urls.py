from django.urls import path, include
from rest_framework.routers import SimpleRouter
from user.views import UserViewSet


urlpatterns = [
    # path('userlist/', UserListView.as_view(), name='user_list'),
    # path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    # path('create_user/', UserCreateView.as_view(), name='user_create'),
    # path('', include(router.urls)),
    # path('users/create/', UserViewSet.as_view({'post': 'create'}), name='users-create'),
    # path('users/delete/<int:pk>/', UserViewSet.as_view({'delete': 'destroy'}), name='users-delete'),
    # path('users/info/<int:pk>/', UserViewSet.as_view({'get': 'retrieve'}), name='users-info'),
]

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns += router.urls
