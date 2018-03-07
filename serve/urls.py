from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.landing,name='landing'),
	url(r'^about',views.about, name='about'),
	url(r'^order',views.order,name='order'),
]