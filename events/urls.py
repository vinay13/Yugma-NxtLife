from django.conf.urls import patterns, url
from events import views


urlpatterns = patterns('',
    url(r'^events/',views.event_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$',views.event_detail)


)
