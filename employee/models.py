from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):

    name = models.CharField(max_length=50)
    employeeId = models.IntegerField()
    position = models.CharField(max_length=100)
    startDate = models.DateField()
    department = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    username = models.ForeignKey(User, on_delete=models.CASCADE,)


    def __str__(self):
        return self.name+'_'+str(self.employeeId)
