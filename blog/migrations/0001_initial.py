# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-24 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('timeposted', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=150)),
            ],
        ),
    ]
