# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0008_auto_20151025_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='contact_number',
            field=models.IntegerField(),
        ),
    ]
