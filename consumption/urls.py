from django.urls import include, re_path
from . import views


urlpatterns = [
        re_path(r'^home/$', views.home, name='home'),
        re_path(r'^login/$', views.login, name='login'),
        re_path(r'^table/$', views.table, name='table'),
        re_path(r'^chart/$', views.chart, name='chart'),
        re_path(r'^unitcal/$', views.unitcal, name='unitcal'),
        re_path(r'^getunit/$', views.getunit, name='getunit'),
        re_path(r'^analysis/$', views.analysis, name='analysis'),
        re_path(r'^analyse/$', views.analyse, name='analyse'),
]