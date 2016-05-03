from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.CourseListView.as_view(), name='course_list'),
   url(r'^(?P<pk>[0-9]+)/$', views.CourseDetailView.as_view(), name='course_detail'),
   url(r'^create/$', views.CourseCreateView.as_view(success_url='/courses/'), name='course_create'),
   url(r'^delete/(?P<pk>[0-9]+)/$', views.CourseDeleteView.as_view(), name='course_delete'),
   url(r'^edit/(?P<pk>[0-9]+)/$', views.CourseEditView.as_view(success_url='/courses/'), name='course_edit'),
]