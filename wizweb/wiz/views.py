from django.shortcuts import render
from django.http import HttpResponse
import json
from models import News,EventGallery
from django.core import serializers

# Create your views here.
def index_req(request):
    all_news_list = list(News.objects.all())
    return render(request,"index.html",{
        "all_news":all_news_list
    })

def home_req(request):
    return render(request,"home.html",{})

def about_req(request):
    all_news_list = list(News.objects.all())
    return render(request,"about.html",{
        "all_news":all_news_list
    })

def event_req(request):
     if request.method == 'GET' and request.GET.has_key('year'):
        print request.path
        year_param = request.GET['year']
        print year_param
        #event_gallery = list(EventGallery.objects.filter(year=year_param))
        #for item in event_gallery:
        #    print "%s %s" % (item.year,item.image)
        #text = {"name":"wuyajie"}
        return HttpResponse(serializers.serialize("json",EventGallery.objects.filter(year=year_param)),content_type="application/json")
     else:
        print "event index"
        return render(request,"event.html",{})



def sponsor_req(request):
    return render(request,"sponsorship.html",{})

def contact_req(request):
    return render(request,"contact.html",{})

def wpc_req(request):
    return render(request,"wpc.html",{})