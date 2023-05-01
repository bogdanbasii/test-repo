from django.views.generic import ListView, DetailView, CreateView
from user.models import User
from django.urls import reverse

# Create your views here.


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class UserCreateView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'age']
    template_name = 'user_form.html'

    def get_success_url(self):
        return reverse('user_list')
