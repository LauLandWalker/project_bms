# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0011_auto_20151027_0313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familymemberinformation',
            name='person',
        ),
        migrations.AddField(
            model_name='familymemberinformation',
            name='civil_status',
            field=models.CharField(max_length=7, choices=[('Married', 'married'), ('Single', 'single')], default='', verbose_name='Civil Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='familymemberinformation',
            name='middle_name',
            field=models.CharField(max_length=100, default='', verbose_name='Middle Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='familymemberinformation',
            name='address',
            field=models.CharField(max_length=120, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='familymemberinformation',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='familymemberinformation',
            name='contact_number',
            field=models.IntegerField(verbose_name='Contact Number'),
        ),
        migrations.AlterField(
            model_name='familymemberinformation',
            name='dob',
            field=models.DateField(verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='familymemberinformation',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='familymemberinformation',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='familymemberinformation',
            name='gender',
            field=models.CharField(max_length=6, choices=[('Male', 'male'), ('Female', 'female')], verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='familymemberinformation',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='dob',
            field=models.DateField(verbose_name='Birthday'),
        ),
    ]
