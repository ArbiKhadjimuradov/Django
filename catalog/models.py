from django.db import models
from users.models import CustomUser


class Category(models.Model):
    """Модель создания таблицы в БД Категория"""
    objects = None
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=500, verbose_name='Описание', null=True)

    def __str__(self):
        return f"Категория: {self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    """Модель создания таблицы в БД Продукты"""
    objects = None
    name = models.CharField(max_length=150, verbose_name='Наименование')  # столбцы таблицы
    description = models.CharField(max_length=500, verbose_name='Описание', null=True)
    picture = models.ImageField(upload_to='media/catalog/photo', verbose_name='Изображение', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        CustomUser,
        verbose_name="Владелец",
        help_text="Укажите владельца продукта",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Статус публикации",
        help_text="Укажите, опубликован ли продукт",
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price', 'created_at']
        permissions = [
            ("can_unpublish_product", "Can_unpublish_product"),
            (
                "can_delete_product",
                "Can delete product",
            ),  # Новое разрешение для удаления
            (
                "can_edit_product",
                "Can edit product",
            ),  # Новое разрешение для редактирования
        ]

    def __str__(self):
        return f"{self.name} - {self.price}₽."
