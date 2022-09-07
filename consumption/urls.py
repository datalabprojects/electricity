from django.urls import include, re_path
from . import views


urlpatterns = [
        re_path(r'^home/$', views.home, name='home'),
        re_path(r'^login/$', views.login, name='login'),
        re_path(r'^form/$', views.form, name='form'),
        re_path(r'^chart/$', views.chart, name='chart'),
]