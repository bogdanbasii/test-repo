import django_filters
from rest_framework import viewsets
from user.models import User
from .pagination import UserPagination
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['first_name', 'last_name', 'age']
    ordering_fields = ['first_name', 'last_name', 'age']
