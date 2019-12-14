from django.contrib import admin
from . models import ShowSeatMatrixModel
# Register your models here.

class ShowSeatMatrixAdminData(admin.ModelAdmin):
    list_display = ('institute_code','choice_code','vacant_seats','lateral_seats')
admin.site.register(ShowSeatMatrixModel , ShowSeatMatrixAdminData )
 