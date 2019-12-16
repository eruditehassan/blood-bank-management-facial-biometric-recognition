from django.db import models
from django.contrib.auth.models import User
from Receptionist.models import Donation_Record
choice = ((1,1),(2,2),(3,3))
Blood_group = (("A+","A+")
,("A-","A-")
,("B+","B+")
,("B-","B-")
,("O+","O+")
,("O-","O-")
,("AB+","AB+")
,("AB-","AB-"))
class Laboratorist(models.Model):
    status = models.IntegerField(choices=choice)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class report_analysis(models.Model):
    analyst = models.ForeignKey(Laboratorist, on_delete=models.CASCADE)
    requested_report = models.OneToOneField(Donation_Record,on_delete=models.CASCADE)
    Blood_group = models.CharField( max_length=3,choices = Blood_group)
    additional_note = models.TextField();
