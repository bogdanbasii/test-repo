from django.urls import path
from .views import PurchaseListView, PurchaseDetailView, PurchaseCreateView

urlpatterns = [
    path('purchaselist/', PurchaseListView.as_view(), name='purchase_list'),
    path('<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
path('create_purchase/', PurchaseCreateView.as_view(), name='purchase_create'),
]
