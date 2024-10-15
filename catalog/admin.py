from django.contrib import admin
from catalog.models import Product, Category, ProductOrder


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active',)
    list_filter = ('title', 'category')
    search_fields = ('title', 'category')


@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'create_at',)
    list_filter = ('product', 'user')
    search_fields = ('product',)
