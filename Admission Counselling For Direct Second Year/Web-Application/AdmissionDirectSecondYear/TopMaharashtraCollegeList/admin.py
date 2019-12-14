from django.contrib import admin
from . models import TopMaharashtraCollegeListModel
# Register your models here.

class TopMaharashtraCollegeListAdminData(admin.ModelAdmin):
    list_display = ('merit_no','marks')
admin.site.register(TopMaharashtraCollegeListModel , TopMaharashtraCollegeListAdminData )
