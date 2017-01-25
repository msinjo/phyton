#from django.conf.urls import url
from django.conf.urls import include, url
from app1 import views
#from . import views

urlpatterns = [
    url(r'^ipaddress/$', views.index, name='ipaddress_list'),
]

#urlpatterns = [
#    url(r'^$', views.index, name='index'),
#    url(r'^ipaddress/$', views.ipaddress, name='ipaddress_list'),
#    url(r'^ipaddress/change/(?P<ipaddress_id>\d+)/$', views.ipaddress_change, name='ipaddress_change'),
#]

