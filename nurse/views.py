import json
from random import randint 
from django.shortcuts import render,redirect
from django.http import JsonResponse
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
    return render(request, "withdrawl.html",{"report":report,"analysis":analysis[0]})
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

    
    return render(request, "Sign In.html")
def home(request):
  if len(Nurse.objects.filter(user = request.user))==1:
    Reports = Donation_Record.objects.filter(status  = "Fit")
    return render(request, "nurse_dashboard.html",{"reports":Reports})
  else:
    return redirect("/nurse")
def withdraw(request):
  pk = request.POST["ScanResult"]
  a = Donation_Record.objects.filter(pk = int(pk))
  if a[0]:
      a[0].status = "withdrawn"
  nurses = Nurse.objects.all()
  print(request.POST)
  for nurse in nurses:
        if nurse.user.username == request.POST["salman"]:
              required = nurse
              withdrawal = Withdrawal()
              withdrawal.nurse = required
              p = Patient()
              p.name = "dummy"
              p.pk = randint(0,10000)
              p.save()
              withdraw.record = a[0]
              withdrawal.patient = p
              withdrawal.save()
              return JsonResponse({"withrawl":"Successfull"})
  return JsonResponse({"withdrawl":"UnsuccessFull"})
def getreport(request):
  x = request.POST["ScanResult"]
  a = Donation_Record.objects.filter(pk = int(x))
  data = {}
  if a[0]:
    
    data["name"] = a[0].Name
    data["age"] = a[0].age
    b = report_analysis.objects.filter(requested_report = a[0])
    data["blood group"] = b[0].Blood_group
  return JsonResponse(data)