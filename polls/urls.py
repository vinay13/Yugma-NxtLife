from django.conf.urls import patterns, url
from polls import views


urlpatterns = [
    url(r'^polls/$',views.poll_list,),
    url(r'^polls(?P<pk>[0-9]+)/$',views.poll_detail),

]

# namespace='router'