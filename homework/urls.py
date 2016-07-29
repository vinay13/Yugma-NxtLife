from django.conf.urls import patterns, url
from homework import views


urlpatterns = [
    url(r'^homework/$',views.homework_list),
    url(r'^homework/(?P<pk>[0-9]+)/$',views.homework_detail),

    url(r'^subjects/$', views.subject_list)

]
