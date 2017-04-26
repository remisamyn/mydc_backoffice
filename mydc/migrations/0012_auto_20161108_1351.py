# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-08 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydc', '0011_auto_20161108_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='visuel',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='contenu',
            name='anneeProduction',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contenu',
            name='casting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contenu',
            name='codeAyantDroit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contenu',
            name='dateSortieVideo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contenu',
            name='droits',
            field=models.ManyToManyField(to='mydc.Droit'),
        ),
        migrations.AlterField(
            model_name='contenu',
            name='imdb',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='contenu',
            name='paysProduction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contenu',
            name='realisateur',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contenu',
            name='synopsis',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contenu',
            name='visuel',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='dateSortieSalle',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='duree',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
