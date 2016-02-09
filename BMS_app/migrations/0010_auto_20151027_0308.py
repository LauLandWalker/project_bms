# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0009_auto_20151025_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='address',
            field=models.CharField(max_length=120, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='age',
            field=models.IntegerField(verbose_name='Age', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='civil_status',
            field=models.CharField(max_length=7, verbose_name='Gender', choices=[('Married', 'married'), ('Single', 'single')]),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='contact_number',
            field=models.IntegerField(verbose_name='Contact Number'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='dob',
            field=models.DateField(verbose_name='Birtday'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='middle_name',
            field=models.CharField(max_length=100, verbose_name='Middle Name'),
        ),
    ]
