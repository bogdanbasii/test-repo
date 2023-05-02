from django.views.generic import ListView, DetailView, CreateView
from .models import Purchase
from django.urls import reverse
from rest_framework import viewsets
from .serializers import PurchaseSerializer
import django_filters


# Create your views here.

class PurchaseFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(lookup_expr='icontains')
    book = django_filters.CharFilter(lookup_expr='icontains')
    date = django_filters.NumberFilter(lookup_expr='exact')
    price = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Purchase
        fields = ['user', 'book', 'date']

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_class = PurchaseFilter
    filterset_fields = ['user', 'book', 'date']
    ordering_fields = ['user', 'book', 'date']

# class PurchaseListView(ListView):
#     model = Purchase
#     template_name = 'purchase_list.html'
#     context_object_name = 'purchases'
#
#
# class PurchaseDetailView(DetailView):
#     model = Purchase
#     template_name = 'purchase_detail.html'
#
#
# class PurchaseCreateView(CreateView):
#     model = Purchase
#     fields = ['user', 'book']
#     template_name = 'purchase_form.html'
#
#     def get_success_url(self):
#         return reverse('purchase_list')
#
