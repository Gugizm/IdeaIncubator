# Generated by Django 5.0.6 on 2024-06-19 22:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_alter_notification_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 19, 22, 5, 9, 195560, tzinfo=datetime.timezone.utc)),
        ),
    ]
