from django.contrib import admin
from . models import WhereAdmissionModel
# Register your models here.

class WhereAdmissionAdminData(admin.ModelAdmin):
    list_display = ('min_percentage',)
admin.site.register(WhereAdmissionModel , WhereAdmissionAdminData )
 