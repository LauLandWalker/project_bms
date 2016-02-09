# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0010_auto_20151027_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='civil_status',
            field=models.CharField(verbose_name='Civil Status', max_length=7, choices=[('Married', 'married'), ('Single', 'single')]),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='gender',
            field=models.CharField(verbose_name='Gender', max_length=6, choices=[('Male', 'male'), ('Female', 'female')]),
        ),
    ]
