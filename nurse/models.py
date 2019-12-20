from django.db import models
from django.contrib.auth.models import User
from Receptionist.models import *
choice = ((1,1),(2,2),(3,3))
Blood_group = (("A+","A+")
,("A-","A-")
,("B+","B+")
,("B-","B-")
,("O+","O+")
,("O-","O-")
,("AB+","AB+")
,("AB-","AB-"))
class Patient(models.Model):
    name = models.CharField( max_length=50)
class Nurse(models.Model):
    status = models.IntegerField(choices=choice)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
class Withdrawal(models.Model):
    record = models.OneToOneField(Donation_Record, on_delete=models.CASCADE)
    date = models.DateTimeField( )
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)