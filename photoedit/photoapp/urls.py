from django.conf.urls import url
from photoapp import views

urlpatterns = [
    url(r'^login/$', views.FacebookLogin.as_view(), name='login'),
    url(r'^photos/$', views.PhotoAppView.as_view(), name='photoview'),
    url(r'^signout/$', views.SignOutView.as_view(), name='signout'),
    url(r'^edit/(?P<id>[0-9]+)/(?P<effects>\w+)?$', views.EditPhotoView.as_view(), name='editphoto'),
    url(r'^delete/(?P<public_id>[A-Za-z0-9]+)/(?P<id>[0-9]+)$', views.DeletePhotoView.as_view(), name='delete'),
]