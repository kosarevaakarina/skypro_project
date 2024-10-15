from django.views.generic import ListView

from catalog.models import Product


class ProductsListView(ListView):
    """Представление для просмотра списка товаров"""
    model = Product
    extra_context = {
        "title": "Каталог товаров"
    }

