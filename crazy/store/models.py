from django.db import models

# Create your models here.
class userdata(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField() 
    Password=models.CharField(max_length=100) 
    class Meta:
        db_table="userdata"

# Create your models here.
class taskdata(models.Model):
    Task=models.CharField(max_length=100)
    Date=models.DateField()
    Time=models.TimeField()
    class Meta:
        db_table="taskdata"