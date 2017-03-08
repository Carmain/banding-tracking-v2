# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-10 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170209_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='supposed_sex',
            field=models.CharField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Undetermined')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='observation',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='coordinate_x',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='coordinate_y',
            field=models.FloatField(null=True),
        ),
    ]