# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0014_auto_20151027_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymemberinformation',
            name='id',
            field=models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='id',
            field=models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False),
        ),
    ]
