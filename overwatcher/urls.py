from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from servers import urls as servers_url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^servers/', include(servers_url)),
]
