# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-06 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('score', models.DecimalField(decimal_places=3, max_digits=4)),
            ],
        ),
    ]
