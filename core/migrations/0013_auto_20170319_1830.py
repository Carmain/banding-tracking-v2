# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170319_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plover',
            name='banding_date',
            field=models.DateField(blank=True, null=True, verbose_name='Banding date'),
        ),
    ]