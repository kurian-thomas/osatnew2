# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-14 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osat', '0004_auto_20171214_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='attending',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'No'), ('Maybe', 'Maybe')], default='Yes', max_length=6),
        ),
    ]