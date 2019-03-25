# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-22 04:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medicals', '0002_auto_20181230_1233'),
        ('medicines', '0002_auto_20190120_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='supplied_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicals.Medical'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 1, 22, 4, 23, 42, 196325, tzinfo=utc)),
        ),
    ]