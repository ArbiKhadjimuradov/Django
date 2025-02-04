from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_customuser_username"),
    ]
    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="username",
        ),
    ]