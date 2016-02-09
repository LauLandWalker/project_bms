# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0015_auto_20151027_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymemberinformation',
            name='id',
            field=models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='id',
            field=models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False),
        ),
    ]
