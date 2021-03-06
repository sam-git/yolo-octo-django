from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yellowdjango.views.home', name='home'),
    # url(r'^yellowdjango/', include('yellowdjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    ('^pages/', include('django.contrib.flatpages.urls')),

    url(r'api/', include('backend.urls', namespace='api')),
    
    (r'^(?P<identifier>.*/)$', 'frontend.views.call_api'),
)

# urlpatterns += patterns('django.contrib.flatpages.views',
#     (r'^(?P<url>.*/)$', 'flatpage'),
# )
