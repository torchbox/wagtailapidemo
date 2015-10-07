from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^register_device/$', views.register_device, name='register_device')
]
