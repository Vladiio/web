from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^question/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^signup/$', views.register, name='register'),
    url(r'^login/$', views.login_view, name='login'),



]

