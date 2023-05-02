from django.urls import path, include
from .views import PurchaseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'purchases', PurchaseViewSet)

urlpatterns = [
    # path('purchaselist/', PurchaseListView.as_view(), name='purchase_list'),
    # path('<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    # path('create_purchase/', PurchaseCreateView.as_view(), name='purchase_create'),
    path('', include(router.urls))
]
