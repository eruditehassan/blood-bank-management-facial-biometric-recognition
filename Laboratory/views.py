from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib import auth
from .models import *
from Receptionist.models import *
def details(request,pk):
    Reports = Donation_Record.objects.all()
    required = 0
    for report in Reports:
        if report.pk  == pk:
            required = report
            break
    return render(request, "report_details.html",{"report":report})
def signin(request):
    if request.method =="POST":
        upassword  = request.POST["psw"]
        uname = request.POST["name"]
        ruser = auth.authenticate(username = uname, password =  upassword)
        laboratorists = Laboratorist.objects.all()
        print(ruser)
        required = 0
        for laboratorist in laboratorists:
            if laboratorist.user == ruser:
                required = laboratorist
                break
        if ruser and required: 
            auth.login(request,ruser)
            return redirect(home)

    
    return render(request, "signin.html")
def home(request):
    Reports = Donation_Record.objects.all()
    return render(request, "lab_dashboard.html",{"reports":Reports})