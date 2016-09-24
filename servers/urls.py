from django.conf.urls import url

from .views import index
from .views import server_status

urlpatterns = [
    url(r'^status/', server_status),
    url(r'^$', index),
]