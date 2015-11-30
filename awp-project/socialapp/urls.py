from django.conf.urls import url

from socialapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_details, name='post_details'),
]
