from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from polls import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eestec_site.views.home', name='home'),
    # url(r'^eestec_site/', include('eestec_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^secret/', views.secret, name='secret'),
    url(r'^searc/', views.search_index, name='search'),
    url(r'^search/(?P<title>\w+)/(?P<author>\w+)/(?P<year>\d{4})/$', views.search_by, name='search_by'),
)
