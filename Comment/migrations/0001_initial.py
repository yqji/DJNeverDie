# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(1, 'NORMAL'), (0, 'DELETED'), (-1, 'UNKNOWN')], default=1)),
                ('create_ts', models.DateTimeField(auto_now_add=True)),
                ('update_ts', models.DateTimeField(auto_now=True)),
                ('owner', models.CharField(default='Anonym', max_length=100, verbose_name='comment publisher')),
                ('to_comment_id', models.IntegerField(default=0, verbose_name='to comment id')),
                ('content', models.TextField(max_length=10000, verbose_name='content')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Article.Article', verbose_name='article')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
