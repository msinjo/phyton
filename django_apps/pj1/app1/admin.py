from django.contrib import admin

# Register your models here.

# 追記
from app1.models import Ipaddress

# 追記
#admin.site.register(Ipaddress)

# 以下を追加
class IpaddressAdmin(admin.ModelAdmin):
    list_display = ('ipaddress', 'status', 'description')

admin.site.register(Ipaddress, IpaddressAdmin)
