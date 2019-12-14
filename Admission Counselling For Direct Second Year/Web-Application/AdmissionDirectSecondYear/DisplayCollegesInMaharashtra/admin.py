from django.contrib import admin
from . models import DisplayCollegesInMaharashtraModel
# Register your models here.
class DisplayCollegesInMaharashtraAdminData(admin.ModelAdmin):
    list_display = ('choice_code','seat_intake')
admin.site.register(DisplayCollegesInMaharashtraModel , DisplayCollegesInMaharashtraAdminData )
