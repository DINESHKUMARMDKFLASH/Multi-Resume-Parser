from django.db import models


# Create your models here.
class Students(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mail = models.EmailField()
    phno = models.CharField(max_length=100)
    st = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    edu = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    workexp = models.CharField(max_length=100)

class Meta:
    db_table = "students"
