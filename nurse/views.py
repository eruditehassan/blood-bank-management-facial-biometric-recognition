from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib import auth
from .models import *
from Receptionist.models import *
from Laboratory.models import *
from django.db.models.functions import datetime
def details(request,pk):
  if len(Nurse.objects.filter(user = request.user))==1:
    if request.method =="POST":
        w =   Withdrawal()
        for x in (Nurse.objects.filter(user  = request.user)):
            w.nurse = x
            if Patient.objects.filter(id = request.POST["id"])[0] :
                w.patient = Patient.objects.filter(id = request.POST["id"])[0]
                w.date = datetime.Now()
    Reports = Donation_Record.objects.filter(status = "Fit")
    required = 0
    for report in Reports:
        if report.pk  == pk:
            required = report
            break
    analysis = report_analysis.objects.filter(requested_report = required)
    return render(request, "withdrawal.html",{"report":report,"analysis":analysis})
  else:
    return redirect("/nurse")
def signin(request):
    if request.method =="POST":
        upassword  = request.POST["psw"]
        uname = request.POST["name"]
        ruser = auth.authenticate(username = uname, password =  upassword)
        Nurses = Nurse.objects.all()
        print(ruser)
        required = 0
        for laboratorist in Nurses:
            if laboratorist.user == ruser:
                required = laboratorist
                break
        if ruser and required: 
            auth.login(request,ruser)
            return redirect(home)

    
    return render(request, "signin.html")
def home(request):
  if len(Nurse.objects.filter(user = request.user))==1:
    Reports = Donation_Record.objects.filter(status  = "Fit")
    return render(request, "lab_dashboard.html",{"reports":Reports})
  else:
    return redirect("/nurse")