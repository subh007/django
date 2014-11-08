from django.conf.urls import patterns, include, url
from volunteer.views import volunteerview

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ivolunteer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^volunteer/$', volunteerview)
)
