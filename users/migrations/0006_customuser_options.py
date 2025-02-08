from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_remove_customuser_username"),
    ]
    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]