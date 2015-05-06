# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_index', models.IntegerField(default=-1)),
                ('year', models.CharField(max_length=4)),
                ('quarter', models.CharField(max_length=1)),
                ('message', models.CharField(max_length=200)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
    ]
