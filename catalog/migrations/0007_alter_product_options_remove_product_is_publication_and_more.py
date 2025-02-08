# Generated by Django 5.1.5 on 2025-02-08 13:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_product_description"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "price", "created_at"],
                "permissions": [
                    ("can_unpublish_product", "Can_unpublish_product"),
                    ("can_delete_product", "Can delete product"),
                    ("can_edit_product", "Can edit product"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.RemoveField(
            model_name="product",
            name="is_publication",
        ),
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(
                default=False,
                help_text="Укажите, опубликован ли продукт",
                verbose_name="Статус публикации",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="catalog.category",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(max_length=500, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите владельца продукта",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="picture",
            field=models.ImageField(
                null=True, upload_to="catalog/photo/", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
