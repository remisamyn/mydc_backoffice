# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-08 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydc', '0010_auto_20161108_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenu',
            name='svodEnd',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contenu',
            name='svodStart',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contenu',
            name='vodEnd',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contenu',
            name='vodStart',
            field=models.DateField(blank=True, null=True),
        ),
    ]
