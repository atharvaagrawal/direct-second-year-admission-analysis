from django.contrib import admin
from . models import CuttOffListModel
# Register your models here.

#admin.site.register(TopCollegesModel)

class CuttOffListAdminData(admin.ModelAdmin):
    list_display = ('institute_code','choice_code')
admin.site.register(CuttOffListModel , CuttOffListAdminData )
