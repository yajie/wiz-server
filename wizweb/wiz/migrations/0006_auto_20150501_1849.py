# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from wiz.models import  EventGalleryDetail

def init_event_gallery_detail(apps, schema_editor):
    init_melamine_2013()
    init_starch_2013()
    init_ethanol_2014()
    init_plasticizer_2014()
    init_starch_2014()
    init_wa_2014()
    init_wpc_2014()
    init_plasticizer_2015()

def init_plasticizer_2015():
    data = ["DSC00840.JPG","DSC00844.JPG","DSC00849.JPG","DSC00859.JPG","DSC00872.JPG","DSC00933.JPG"]
    init_model_and_save(data,2015,"plasticizer")

def init_ethanol_2014():
    data = ["DSC00077.JPG","DSC00092.JPG","DSC00100.JPG","DSC00118.JPG","DSC00137.JPG","DSC00143.JPG"]
    init_model_and_save(data,2014,"ethanol")

def init_plasticizer_2014():
    data = ["IMG_1653.JPG","IMG_3643.JPG","IMG_3657.JPG","IMG_3658.JPG","IMG_3662.JPG","IMG_3679.JPG"]
    init_model_and_save(data,2014,"plasticizer")

def init_starch_2014():
    data = ["IMG_8001.JPG","IMG_8026.JPG","IMG_8042.JPG","IMG_8050.JPG","IMG_8262.JPG","IMG_8306.JPG"]
    init_model_and_save(data,2014,"starch")

def init_wa_2014():
    data = ["IMG_7033.JPG","IMG_7043.JPG","IMG_7046.JPG","IMG_7077.JPG","IMG_7083.JPG","IMG_7107.JPG","IMG_7113.JPG","IMG_7139.JPG","IMG_7143.JPG"]
    init_model_and_save(data,2014,"wa")

def init_wpc_2014():
    data = ["IMG_3933.JPG","IMG_3967.JPG","IMG_3969.JPG","IMG_4019.JPG","IMG_4038.JPG","IMG_4112.JPG","P1060749.JPG","P1060754.JPG","P1060767.JPG"]
    init_model_and_save(data,2014,"wpc")

def init_melamine_2013():
    data = ["DSC03991.JPG","IMG_2779.JPG","IMG_2785.JPG"]
    init_model_and_save(data,2013,"melamine")

def init_starch_2013():
    data = ["DSC03660.JPG","DSC03664.JPG","DSC03686.JPG","DSC03736.JPG","DSC03738.JPG","IMG_1965.JPG"]
    init_model_and_save(data,2013,"starch")


def init_model_and_save(event_data,year,conference):
    for index in range(len(event_data)):
        model = EventGalleryDetail()
        model.year = year
        model.data_index = index + 1
        model.image = event_data[index]
        model.conference = conference
        model.save()

class Migration(migrations.Migration):

    dependencies = [
        ('wiz', '0005_eventgallerydetail'),
    ]

    operations = [
        migrations.RunPython(init_event_gallery_detail),
    ]
