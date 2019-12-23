import os
import urllib3
import requests
import shutil
from django.core.files import File
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib import auth
from .models import *
from Receptionist.models import *
def details(request,pk):
    if len(Laboratorist.objects.filter(user = request.user))==1:
        if request.method == "POST":
            report = report_analysis()
            report.Blood_group = request.POST["blood group"]
        
            for analyst in Laboratorist.objects.filter(user = request.user):
                report.analyst = analyst
                for record in Donation_Record.objects.filter(pk = pk, status = "Pending"):
                    

                    response = response = requests.get("http://barcodes4.me/barcode/c128b/"+str(pk)+".png",stream = True)
                    with open('tmp_img.png', 'wb') as f:
                        shutil.copyfileobj(response.raw, f)

                    with open('tmp_img.png', 'rb') as f:
                        image_file = File(f) 
                        record.barcode.save("demo.png",image_file)
                    os.remove('tmp_img.png')
                    report.requested_report = record
                    report.additional_record = request.POST["report"]
                    report.save()
         
        Reports = Donation_Record.objects.all()
        required = 0
        for report in Reports:
            if report.pk  == pk:
                required = report
                break
        return render(request, "report_details.html",{"report":report})
    else:
        return redirect("/laboratory")
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

    
    return render(request, "Sign In.html")
def home(request):
    if len(Laboratorist.objects.filter(user = request.user))==1:
        Reports = Donation_Record.objects.filter(status = "Pending")
        return render(request, "lab_dashboard.html",{"reports":Reports})
    else:
        return redirect("/laboratory")
def barcode(pk):
    url = 'http://barcodes4.me/barcode/c128b/'+str(pk)+'.gif'
    response = requests.get(url, stream=True)
    return  response.raw
