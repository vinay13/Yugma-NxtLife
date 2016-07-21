from django.conf.urls import patterns, url
from polls import views


urlpatterns = [
    url(r'^polls/$',views.poll_list),

]