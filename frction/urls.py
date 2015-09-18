from django.conf.urls import url

from frction import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]