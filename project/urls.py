# coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^admin/', include(admin.site.urls)),
    url('^ranking/', include('ranking_real_time.urls')),
    url('^blog/', include('acrux_blog.urls')),
    url('^grappelli/', include('grappelli.urls')),
]
