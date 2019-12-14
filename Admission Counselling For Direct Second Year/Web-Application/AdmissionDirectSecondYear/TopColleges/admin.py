from django.contrib import admin
from . models import TopCollegesModel
# Register your models here.

#admin.site.register(TopCollegesModel)

class TopCollegesAdminData(admin.ModelAdmin):
    list_display = ('score','crank')
admin.site.register(TopCollegesModel , TopCollegesAdminData )
