from django.conf.urls import url

from . import views

app_name = 'UserLogin'

urlpatterns = [

	url(r'^$',views.indexView,name='home'),
	
	url(r'^register/$',views.registerView,name='register'),

	url(r'^login/$',views.loginView,name='login'),
]