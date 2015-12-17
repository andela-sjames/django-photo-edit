from django.conf.urls import url
from photoapp import views, effects

urlpatterns = [
    url(r'^login/$', views.FacebookLogin.as_view(), name='login'),
    url(r'^photos/$', views.PhotoAppView.as_view(), name='photoview'),
    url(r'^signout/$', views.SignOutView.as_view(), name='signout'),
    url(r'^delete/(?P<public_id>[A-Za-z0-9]+)/(?P<id>[0-9]+)$',
        views.DeletePhotoView.as_view(), name='delete'),
    url(r'^addeffects/$', effects.PillowImageView.as_view(), name='addeffects')
]
