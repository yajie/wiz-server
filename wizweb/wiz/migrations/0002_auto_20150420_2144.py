# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from wiz.models import News

def init_news(apps, schema_editor):
    ethonalItem = News()
    ethonalItem.data_index = 0
    ethonalItem.year = 2015
    ethonalItem.message = "Ethanol & Biofuels Asia 2015 will be held on July 8-9,in Manila Philippines."
    ethonalItem.save()

    soyaItem = News()
    soyaItem.data_index = 1
    soyaItem.year = 2015
    soyaItem.message = "Soya Asia is coming."
    soyaItem.save()

class Migration(migrations.Migration):

    dependencies = [
        ('wiz', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_news),
    ]
