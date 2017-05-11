# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0003_utilisateur_true_ad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='true_ad',
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='adresse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='utilisateurs.Adresse'),
        ),
    ]
