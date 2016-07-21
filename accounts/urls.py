from django.conf.urls import patterns, url
from accounts import views


urlpatterns = [
    url(r'^accounts/$',views.UserList.as_view()),
    url(r'^accounts/(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),

]
