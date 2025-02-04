from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_remove_customuser_username"),
    ]
    operations = [
        migrations.AddField(
            model_name="customuser",
            name="username",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]