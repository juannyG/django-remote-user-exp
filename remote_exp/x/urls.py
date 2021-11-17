from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.login_view, name='login_view'),
    url(r'^secret1$', views.secret_view_1, name='secret_view_1'),
    url(r'^secret2$', views.secret_view_2, name='secret_view_2'),
    url(r'^logout$', views.logout_view, name='logout_view'),
)
