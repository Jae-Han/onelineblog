from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^blog/$', 'blog.views.index'),
        url(r'^blog/submit/$', 'blog.views.submit'),
        url(r'^blog/(?P<article_id>\d+)/remove/$', 'blog.views.remove'),
        url(r'^admin/', include(admin.site.urls)),
)
