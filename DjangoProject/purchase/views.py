from django.views.generic import ListView, DetailView, CreateView
from .models import Purchase
from django.urls import reverse


# Create your views here.

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'purchase_list.html'
    context_object_name = 'purchases'


class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'purchase_detail.html'


class PurchaseCreateView(CreateView):
    model = Purchase
    fields = ['user', 'book']
    template_name = 'purchase_form.html'

    def get_success_url(self):
        return reverse('purchase_list')

