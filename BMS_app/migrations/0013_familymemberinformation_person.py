# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0012_auto_20151027_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymemberinformation',
            name='person',
            field=models.ForeignKey(default='', to='BMS_app.PersonalInformation'),
            preserve_default=False,
        ),
    ]
