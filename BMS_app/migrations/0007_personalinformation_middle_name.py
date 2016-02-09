# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0006_auto_20151025_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='middle_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
