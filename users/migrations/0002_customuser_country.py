from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]
    operations = [
        migrations.AddField(
            model_name="customuser",
            name="country",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]