from django.conf.urls import patterns, url
from chat import views


urlpatterns = [
    url(r'^messages/$',views.MessageView),
    
]






