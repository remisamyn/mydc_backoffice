# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydc', '0005_auto_20161028_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('contenus', models.ManyToManyField(to='mydc.Contenu')),
            ],
        ),
    ]
