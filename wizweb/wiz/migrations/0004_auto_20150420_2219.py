# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from wiz.models import EventGallery

def init_event_gallery(apps, schema_editor):
    #2015
    conf_event_2015 = EventGallery()
    conf_event_2015.year = 2015
    conf_event_2015.quarter = 1
    conf_event_2015.image = "plasticizer_2015.jpg"
    conf_event_2015.conference = "plasticizer"
    conf_event_2015.data_index = 1
    conf_event_2015.save()

    # 2014
    conf_event_2014_1 = EventGallery()
    conf_event_2014_1.year = 2014
    conf_event_2014_1.quarter = 1
    conf_event_2014_1.image = "plasticizer_2014.jpg"
    conf_event_2014_1.conference = "plasticizer"
    conf_event_2014_1.data_index = 1
    conf_event_2014_1.save()

    conf_event_2014_2 = EventGallery()
    conf_event_2014_2.year = 2014
    conf_event_2014_2.quarter = 2
    conf_event_2014_2.image = "wpc_2014.jpg"
    conf_event_2014_2.conference = "wood plastic composite"
    conf_event_2014_2.data_index = 2
    conf_event_2014_2.save()

    conf_event_2014_3 = EventGallery()
    conf_event_2014_3.year = 2014
    conf_event_2014_3.quarter = 3
    conf_event_2014_3.image = "wa_2014.jpg"
    conf_event_2014_3.conference = "wood adhesive"
    conf_event_2014_3.data_index = 3
    conf_event_2014_3.save()

    conf_event_2014_4 = EventGallery()
    conf_event_2014_4.year = 2014
    conf_event_2014_4.quarter = 4
    conf_event_2014_4.image = "starch_2014.jpg"
    conf_event_2014_4.conference = "starch"
    conf_event_2014_4.data_index = 4
    conf_event_2014_4.save()

    conf_event_2014_5 = EventGallery()
    conf_event_2014_5.year = 2014
    conf_event_2014_5.quarter = 4
    conf_event_2014_5.image = "ethanol_2014.jpg"
    conf_event_2014_5.conference = "ethanol"
    conf_event_2014_5.data_index = 5
    conf_event_2014_5.save()

    # 2013
    conf_event_2013_1 = EventGallery()
    conf_event_2013_1.year = 2013
    conf_event_2013_1.quarter = 4
    conf_event_2013_1.image = "starch_2013.jpg"
    conf_event_2013_1.conference = "starch"
    conf_event_2013_1.data_index = 1
    conf_event_2013_1.save()

    conf_event_2013_2 = EventGallery()
    conf_event_2013_2.year = 2013
    conf_event_2013_2.quarter = 4
    conf_event_2013_2.image = "melamine_2013.jpg"
    conf_event_2013_2.conference = "melamine"
    conf_event_2013_2.data_index = 2
    conf_event_2013_2.save()

class Migration(migrations.Migration):

    dependencies = [
        ('wiz', '0003_eventgallery'),
    ]

    operations = [
        migrations.RunPython(init_event_gallery),
    ]
