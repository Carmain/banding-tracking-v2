# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-08 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170210_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='observation',
            options={'ordering': ['-date']},
        ),
        migrations.AlterUniqueTogether(
            name='observer',
            unique_together=set([('last_name', 'first_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='plover',
            unique_together=set([('metal_ring', 'code', 'color')]),
        ),
    ]
