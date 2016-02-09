# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0013_familymemberinformation_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='dob',
            field=models.DateField(),
        ),
    ]
