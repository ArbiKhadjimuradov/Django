import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_product_owner"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(
                blank=True, max_length=500, null=True, verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="product",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="picture",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="catalog/photo/",
                verbose_name="Изображение",
            ),
        ),
    ]