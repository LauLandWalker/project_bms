# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0017_auto_20151030_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymemberinformation',
            name='relation',
            field=models.CharField(max_length=9, verbose_name='Relation', choices=[('Mother', 'mother'), ('Father', 'father'), ('Father', 'siblings')]),
        ),
    ]
