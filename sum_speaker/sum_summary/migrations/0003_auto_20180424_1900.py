# Generated by Django 2.0.4 on 2018-04-24 10:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sum_summary', '0002_auto_20180424_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='reg_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 24, 19, 0, 58, 808797)),
        ),
        migrations.AlterField(
            model_name='member',
            name='reg_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 24, 19, 0, 58, 808797)),
        ),
        migrations.AlterField(
            model_name='member',
            name='update_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 24, 19, 0, 58, 808797)),
        ),
    ]
