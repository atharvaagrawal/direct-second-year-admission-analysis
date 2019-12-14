from django.db import models

# Create your models here.


class ShowSeatMatrixModel(models.Model):
    main_group = models.IntegerField()
    sub_group = models.IntegerField()
    institute_code = models.IntegerField()
    institute_name = models.CharField(max_length=300)
    choice_code = models.IntegerField() 
    status = models.CharField(max_length=300)
    vacant_seats = models.IntegerField()
    lateral_seats  = models.IntegerField()
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
        db_table = "SeatAlloatment2019" 