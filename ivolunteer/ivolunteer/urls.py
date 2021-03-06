from django.conf.urls import patterns, include, url
from volunteer.views import volunteerview, volunteer_name

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ivolunteer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # learn https://docs.djangoproject.com/en/dev/topics/http/urls/#captured-parameters

    url(r'^admin/', include(admin.site.urls)),
    url(r'^volunteer/$', volunteerview),
    url(r'^volunteername/(?P<name>\w+)/$', volunteer_name),
)
