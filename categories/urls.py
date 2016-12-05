from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.categories_list, name='categories_list'),
    url(r'^(?P<slug>[\w-]+)/$', views.single_category, name='single_category'),
]
