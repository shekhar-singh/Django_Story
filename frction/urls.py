from django.conf.urls import url
from frction import views
from django.contrib import admin


urlpatterns = [
    url(r'^login/', views.login ,name='login'),
    url(r'^auth/$', views.auth_view,name='auth'),
    url(r'^logout/$', views.logout,name='logout'),
    url(r'^loggedin/$', views.loggedin,name='loggedin'),
    url(r'^invalid/$', views.invalid_login,name='invalid'),
    url(r'^register/$', views.register_user,name='register'),
    url(r'^success/$', views.success,name='success'),

]