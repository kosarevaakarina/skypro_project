from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductsListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='product_list'),
]