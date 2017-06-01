from django.conf.urls import url

from . import views
from .views import UserViewSet
app_name = 'delegation'
urlpatterns = [

    url(r'^$', UserViewSet.as_view({'get': 'list'})),
    url(r'^(?P<email>[^ /]+)/folders$', UserViewSet.as_view({'get': 'getFolders'})),
    url(r'^(?P<email>[^ /]+)/folders/(?P<folder>[a-zA-Z][a-zA-Z0-9]*)$', UserViewSet.as_view({'get': 'getFoldersDetails'})),
    url(r'^(?P<email>[^ /]+)/folders/(?P<folder>[a-zA-Z][a-zA-Z0-9]*)/helpers$', UserViewSet.as_view({'get': 'getHelperForFolder'}))

    # url(r'^$', views.users, name='index'),
    # url(r'^(?P<email>[^ /]+)$', views.abc, name='abc')
]