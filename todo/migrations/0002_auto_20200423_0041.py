# Generated by Django 3.0.5 on 2020-04-22 23:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_to_do',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 23, 40, 59, 538513, tzinfo=utc)),
        ),
    ]
