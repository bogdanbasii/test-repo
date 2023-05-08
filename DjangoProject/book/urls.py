from django.urls import path, include
from .views import BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = [
    # path('booklist/', BookListView.as_view(), name='book_list'),
    # path('<int:id>/', BookDetailView.as_view(), name='book_detail'),
    # path('create_book/', BookCreateView.as_view(), name='book_create'),
    path('', include(router.urls)),
]
