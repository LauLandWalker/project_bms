# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0016_auto_20151027_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymemberinformation',
            name='relation',
            field=models.CharField(verbose_name='Relation', default='', max_length=9, choices=[('Mother', 'married'), ('Father', 'single'), ('Father', 'siblings')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='familymemberinformation',
            name='person',
            field=models.ForeignKey(to='BMS_app.PersonalInformation', null=True),
        ),
    ]
