# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_addressvizrequest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addressvizrequest',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='addressvizrequest',
            name='tx_limit',
            field=models.IntegerField(default=50),
        ),
    ]
