from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
