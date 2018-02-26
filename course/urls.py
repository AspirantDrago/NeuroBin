from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.course_list, name='course_list'),
	url(r'^api/add/(?P<name>\w+)/val=(?P<val>[\d,\.]+)&prop=(?P<prop>\d+)$', views.course_add, name='course_add'),
	url(r'^api/clear/(?P<name>\w+)$', views.course_clear, name='course_add'),
	url(r'^course/(?P<name>[\w,\%]+)$', views.course_view, name='course_view'),
]