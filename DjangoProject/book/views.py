from django.shortcuts import render
from .models import Book
from django.http import JsonResponse


# Create your views here.

def get_all_books(request):
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False)
