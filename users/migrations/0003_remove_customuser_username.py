from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_customuser_country"),
    ]
    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="username",
        ),
    ]