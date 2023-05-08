import django_filters
from rest_framework import viewsets

from user.models import User
from .pagination import UserPagination
from .serializers import UserSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['first_name', 'last_name', 'age']
    ordering_fields = ['first_name', 'last_name', 'age']



# class UserListView(ListView):
#     model = User
#     template_name = 'user_list.html'
#     context_object_name = 'users'
#
#
# class UserDetailView(DetailView):
#     model = User
#     template_name = 'user_detail.html'
#
#
# class UserCreateView(CreateView):
#     model = User
#     fields = ['first_name', 'last_name', 'age']
#     template_name = 'user_form.html'
#
#     def get_success_url(self):
#         return reverse('user_list')
