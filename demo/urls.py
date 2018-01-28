from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.demo, name='demo'),
    url(r'^/home/$', views.home, name='home'),
    url(r'^/contacts/$', views.contacts, name='contacts'),
]
