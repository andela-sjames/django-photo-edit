from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from photoapp import views
import photoapp.urls

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^photoapp/', include(photoapp.urls)),
    url(r'^$', views.HomeView.as_view(), name='homepage'),
)

if settings.DEBUG:
        urlpatterns += patterns('',
                                url(r'^media/(?P<path>.*)$',
                                    'django.views.static.serve', {
                                        'document_root': settings.MEDIA_ROOT,
                                    }),
                                url(r'^static/(?P<path>.*)$',
                                    'django.views.static.serve', {
                                        'document_root': settings.STATIC_ROOT,
                                    }),
                                )

handler404 = 'photoapp.views.custom_404'
handler500 = 'photoapp.views.custom_500'
