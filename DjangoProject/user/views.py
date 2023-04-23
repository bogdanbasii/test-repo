from .models import User
from django.http import JsonResponse


# Create your views here.

def get_all_users(request):
    users = list(User.objects.values())
    return JsonResponse(users, safe=False)