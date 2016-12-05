from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.projects_list, name='projects_list'),
    url(r'^my/$', views.my_projects, name='my_projects'),
    url(r'^add/$', views.create_project, name='create_project'),
    url(r'^(?P<slug>[\w-]+)/$', views.single_project, name='single_project'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.edit_project, name='edit_project'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.delete_project, name='delete_project'),
]
