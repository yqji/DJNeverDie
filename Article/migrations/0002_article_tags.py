# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tag', '0001_initial'),
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='Tag.Tag'),
        ),
    ]