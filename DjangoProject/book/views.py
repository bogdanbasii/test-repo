from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Book
from django.urls import reverse


# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    pk_url_kwarg = 'id'


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'year', 'price']
    template_name = 'book_form.html'

    def get_success_url(self):
        return reverse('book_list')

