# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-28 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='profile'),
        ),
    ]
