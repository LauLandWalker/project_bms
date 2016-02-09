from django.conf.urls import url
from BMS_app import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='Index'),
    url(r'^listall/$', views.ListAll.as_view(), name='ListAll'),
    url(r'^listall/(?P<pk>\d+)/$', views.PersonDetails.as_view(), name='PersonDetails'),
    url(r'^listall/(?P<pk>\d+)/create/$', views.RelativeCreate.as_view(), name='CreateRelatives'),
    url(r'^create/$', views.CreatePerson.as_view(), name='Create'),
    url(r'^update/(?P<pk>\d+)/$', views.UpdatePerson.as_view(), name='Update'),
    url(r'^update_relative/(?P<pk>\d+)/$', views.UpdateRelative.as_view(), name='UpdateRelative'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeletePerson.as_view(), name='Delete'),
    url(r'^delete_relative/(?P<pk>\d+)/$', views.DeleteRelative.as_view(), name='DeleteRelative'),
    url(r'^about/$', views.About.as_view(), name='About'),
    url(r'^results/$', views.BlogSearchListView.as_view(), name='Result'),




]