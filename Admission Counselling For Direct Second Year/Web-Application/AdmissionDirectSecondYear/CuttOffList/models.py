from django.db import models

# Create your models here.
 
class CuttOffListModel(models.Model):
    institute_code = models.IntegerField()
    institute_name = models.CharField(max_length=300)
    choice_code = models.IntegerField() 
    course_name = models.CharField(max_length=300)
    shift = models.CharField(max_length=300)
    subgroup = models.IntegerField()
    ews = models.FloatField()
    gopen = models.FloatField()
    lopen = models.FloatField()
    gsc = models.FloatField()
    lsc = models.FloatField()
    gst = models.FloatField()
    lst = models.FloatField()
    vjdtnta = models.FloatField()
    ntb = models.FloatField()
    ntc = models.FloatField()
    ntd = models.FloatField()
    obc = models.FloatField()
    sebc = models.FloatField()
  
    class Meta:
        db_table = "CuttOffList2019" 