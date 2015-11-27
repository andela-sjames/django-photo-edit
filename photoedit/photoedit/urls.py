from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from photoapp import views
import photoapp.urls

urlpatterns = patterns('',
    # Examples:
    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^photoapp/', include(photoapp.urls)),
    url(r'^$', views.HomeView.as_view(), name='homepage'),
)


handler404='bucketlist.views.custom_404'
handler500='bucketlist.views.custom_500'
