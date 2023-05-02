from .models import Book
from django.urls import reverse
from rest_framework import viewsets
from .serializers import BookSerializer
import django_filters


# Create your views here.

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    year = django_filters.NumberFilter(lookup_expr='exact')
    price = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'price']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    filterset_fields = ['title', 'author', 'year', 'price']
    ordering_fields = ['title', 'author', 'year', 'price']

# class BookListView(ListView):
#     model = Book
#     template_name = 'book_list.html'
#     context_object_name = 'books'
#
#
# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'book_detail.html'
#     pk_url_kwarg = 'id'
#
#
# class BookCreateView(CreateView):
#     model = Book
#     fields = ['title', 'author', 'year', 'price']
#     template_name = 'book_form.html'
#
#     def get_success_url(self):
#         return reverse('book_list')
#
