# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 12:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_heroinfo_hero_hometown'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heroinfo',
            name='hero_hometown',
        ),
    ]