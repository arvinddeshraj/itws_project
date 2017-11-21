from django.conf.urls import url
from . import views

app_name = 'sensors'

urlpatterns = [

    url(r'^$', views.index,name='index'),

    url(r'^macroreading/$',views.macroSensorView,name='macro'),

    url(r'^microreading/$',views.microSensorView,name='micro'),

    url(r'^addplant/$', views.addPlants,name='addPlants'),

    url(r'^userprofile/$',views.userprofile,name='userprofile'),

    url(r'^addmicroreading/(?P<plant_id>[0-9]+)/$', views.add_reading_micro),

    url(r'^addmacroreading/$', views.add_reading_macro),

]