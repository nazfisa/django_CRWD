from django.conf.urls import url
from advapp import views

app_name= 'advapp'
urlpatterns = [
   
    url(r'^$', views.SchoolListViews.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailViews.as_view(),name='detail'),
    url(r'^create/$', views.SchoolCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateViews.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(),name='delete'),
]