# Generated by Django 5.0.6 on 2024-06-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="updated_date",
            field=models.DateField(auto_now=True),
        ),
    ]