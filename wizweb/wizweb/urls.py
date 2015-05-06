from django.conf.urls import include, url
from django.contrib import admin
from wiz import  views

urlpatterns = [
    # Examples:
    # url(r'^$', 'wizweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index_req),
    url(r'^home/$', views.home_req),
    url(r'^about/$', views.about_req),
    url(r'^event/$', views.event_req),
    url(r'^sponsorship/$', views.sponsor_req),
    url(r'^contact/$', views.contact_req),
    url(r'^wpc/$', views.wpc_req),
]
