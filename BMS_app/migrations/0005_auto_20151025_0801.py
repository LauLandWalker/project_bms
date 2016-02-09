# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0004_auto_20151025_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='civil_status',
            field=models.CharField(max_length=7, choices=[('married', 'married'), ('single', 'single')]),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='gender',
            field=models.CharField(max_length=6, choices=[('male', 'male'), ('female', 'female')]),
        ),
    ]
