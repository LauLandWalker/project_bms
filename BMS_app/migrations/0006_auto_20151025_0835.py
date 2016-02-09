# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0005_auto_20151025_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='civil_status',
            field=models.CharField(choices=[('Married', 'married'), ('Single', 'single')], max_length=7),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=6),
        ),
    ]
