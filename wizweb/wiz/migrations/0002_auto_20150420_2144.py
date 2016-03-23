# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from wiz.models import News

def init_news(apps, schema_editor):
    firstItem = News()
    firstItem.data_index = 0
    firstItem.year = 2016
    firstItem.message = "Ethanol & Biofuels Asia 2016 will be held in Singapore during June 29-30."
    firstItem.save()

    secondItem = News()
    secondItem.data_index = 1
    secondItem.year = 2016
    secondItem.message = "Ethanol Outlook India 2016 will be held in Mumbai during August 19-20."
    secondItem.save()

    thirdItem = News()
    thirdItem.data_index = 2
    thirdItem.year = 2016
    thirdItem.message = "Wiz is now one of the representatives of UL Prospector®- the leading Raw Materials Search Engine"
    thirdItem.save()

    fourthItem = News()
    fourthItem.data_index = 3
    fourthItem.year = 2016
    fourthItem.message = "WoodChem 2016 will be held in Bangkok in October 19-20"
    fourthItem.save()

class Migration(migrations.Migration):

    dependencies = [
        ('wiz', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_news),
    ]
