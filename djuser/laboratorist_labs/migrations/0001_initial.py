# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-04 15:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0004_auto_20181230_1309'),
        ('laboratorists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboratoristLab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=120)),
                ('test_level', models.CharField(max_length=120)),
                ('comment', models.TextField()),
                ('is_done', models.BooleanField(default=False)),
                ('test_date', models.DateField(default=datetime.datetime(2019, 1, 4, 15, 43, 50, 901485, tzinfo=utc))),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patient')),
                ('test_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorists.Laboratorist')),
            ],
        ),
    ]