from django.conf.urls import patterns, include, url
from django.contrib import admin

from links.views import LinkListView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LinkListView.as_view(), name='home'),
)
