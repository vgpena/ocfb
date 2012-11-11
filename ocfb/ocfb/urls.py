from django.conf.urls import patterns, include, url
#from roster.models import Member

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
   	#url(r'^$', 'ocfb.views.index', name='index'),
    #url(r'^ocfb/', include('ocfb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^roster/','ocfb.views.roster', name='roster'),
	
	url(r'^media/', include('daguerre.urls')),
)

if settings.DEBUG:
		urlpatterns += patterns('',
			url (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
				'document_root': settings.MEDIA_ROOT,
			}),
		)

#urlpatterns += patterns('django.contrib.flatpages.views',
#	(r'^(?P<url>.*)$', 'flatpage')
#)