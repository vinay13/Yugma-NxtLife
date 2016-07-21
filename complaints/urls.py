from django.conf.urls import patterns, url
from complaints import views


urlpatterns = [
    url(r'^complaints/$',views.complaint_list),
    url(r'^complaints/(?P<pk>[0-9]+)/$',views.complaint_detail),
    url(r'^comments/$',views.complaintComment_list),
]





