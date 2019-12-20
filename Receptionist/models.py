from django.db import models
from django.contrib.auth.models import User
status_clarity = {(1,1),(2,2),(3,3)}
report_clearance = {("Pending","Pending"),("Fit","Fit"),("UnFit","Unfit"),("withdrawn","withdrawn")}
class Receptionist(models.Model):
    status = models.IntegerField(default=1,choices=status_clarity)
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
class Donation_Record(models.Model):
    Name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField( max_length=13)
    email = models.EmailField( max_length=254)
    cnic = models.CharField(max_length = 13)
    status = models.CharField(default = "Pending", choices =report_clearance,max_length = 13)
    def __str__(self):
        return (str(self.pk))