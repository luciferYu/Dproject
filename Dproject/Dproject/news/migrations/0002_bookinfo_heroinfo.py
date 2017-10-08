# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('book_title', models.CharField(max_length=50)),
                ('book_comment', models.IntegerField(default=0)),
                ('book_read', models.IntegerField(default=0)),
                ('book_delete', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('hero_name', models.CharField(max_length=50)),
                ('hero_sex', models.BooleanField(default=True)),
                ('hero_desc', models.TextField()),
                ('hero_delete', models.BooleanField(default=False)),
                ('hero_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.BookInfo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]