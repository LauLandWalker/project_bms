# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import builtins


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyMemberInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=1)),
                ('address', models.CharField(max_length=120)),
                ('contact_number', models.IntegerField(verbose_name=builtins.max)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='FamilyMember',
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='dob',
            field=models.DateField(verbose_name='Date of Birth', max_length=8),
        ),
        migrations.AddField(
            model_name='familymemberinformation',
            name='person',
            field=models.ForeignKey(to='BMS_app.PersonalInformation'),
        ),
    ]
