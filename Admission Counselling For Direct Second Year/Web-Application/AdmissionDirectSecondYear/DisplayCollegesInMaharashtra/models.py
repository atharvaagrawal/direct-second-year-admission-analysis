from django.db import models

# Create your models here.

 
class DisplayCollegesInMaharashtraModel(models.Model):
    choice_code = models.IntegerField()
    course_name = models.CharField(max_length=300)
    shift = models.CharField(max_length=300)
    seat_intake = models.IntegerField()
    college_name = models.CharField(max_length=300)

    class Meta:
        db_table = "CollegeInMaharashtra2019"  