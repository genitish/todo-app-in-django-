# Generated by Django 2.1 on 2019-03-14 10:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_auto_20190314_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 14, 15, 43, 35, 472561), null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.TimeField(default=datetime.datetime(2019, 3, 14, 10, 13, 35, 472561, tzinfo=utc), null=True),
        ),
    ]
