from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="picture",
            field=models.ImageField(
                null=True, upload_to="catalog/photo/", verbose_name="Изображение"
            ),
        ),
    ]
