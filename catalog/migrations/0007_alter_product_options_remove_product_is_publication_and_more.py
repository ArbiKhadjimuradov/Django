import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_product_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "price", "created_at"],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.RemoveField(
            model_name="product",
            name="is_publication",
        ),
        migrations.RemoveField(
            model_name="product",
            name="owner",
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
