import datetime

from django.db import models

from users.models import User


class Category(models.Model):
    """Модель категории"""
    title = models.CharField(max_length=64, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Модель Товара"""
    title = models.CharField(max_length=64, verbose_name='Название товара')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Категория')
    is_active = models.BooleanField(default=True, verbose_name='Статус активности')
    price = models.IntegerField(null=True, blank=True, verbose_name='Стоимость')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_count_order_last_month(self):
        """Количество заказов за прошлый месяц от текущего"""

        current_day = datetime.datetime.today()
        first_day_current_month = current_day.replace(day=1)
        if current_day.day == 1:
            first_day_last_month = current_day.replace(year=current_day.year - 1, month=12, day=1)
        else:
            first_day_last_month = current_day.replace(month=current_day.month - 1, day=1)
        last_day_last_month = first_day_current_month - datetime.timedelta(days=1)

        count_order_last_month = self.productorder_set.filter(
            create_at__range=(first_day_last_month, last_day_last_month)
        ).count()

        return count_order_last_month

    def get_count_order_current_month(self):
        """Количество заказов за текущий месяц начиная с первого дня"""
        current_date = datetime.datetime.now()
        first_day_current_month = current_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        count_order_current_month = self.productorder_set.filter(
            create_at__gte=first_day_current_month
        ).count()
        return count_order_current_month


class ProductOrder(models.Model):
    """Модель Заказа продукта"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Заказчик')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    create_at = models.DateTimeField(verbose_name='Дата и время заказа')

    def __str__(self):
        return f'{self.product} - {self.user}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
