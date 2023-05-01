from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView

urlpatterns = [
    path('booklist/', BookListView.as_view(), name='book_list'),
    path('<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('create_book/', BookCreateView.as_view(), name='book_create'),
]
