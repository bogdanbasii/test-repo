from django.shortcuts import render

# Create your views here.

from .models import Purchase
from django.http import JsonResponse


# Create your views here.

def get_all_purchases(request):
    purchases = list(Purchase.objects.values('user_id', 'book_id', 'date'))
    return JsonResponse(purchases, safe=False)