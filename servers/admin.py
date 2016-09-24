from django.contrib import admin

from .models import ServerInfo
from .models import ServerNowStatus
from .models import ServerStatus


admin.site.register(ServerInfo)
admin.site.register(ServerNowStatus)
admin.site.register(ServerStatus)