# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20160427_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressVizRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('address', models.TextField()),
                ('path', models.TextField(null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
