# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiz', '0004_auto_20150420_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventGalleryDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_index', models.IntegerField(default=-1)),
                ('year', models.CharField(max_length=4)),
                ('image', models.CharField(max_length=100)),
                ('conference', models.CharField(max_length=50)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
    ]
