from django.conf.urls import patterns, url
from complaints import views


urlpatterns = [
    url(r'^complaints/$',views.ComplaintList.as_view()),
    url(r'^complaints/(?P<pk>[0-9]+)/$',views.complaint_detail),
    url(r'^complaints/comments/$',views.complaintComment_list),
]





