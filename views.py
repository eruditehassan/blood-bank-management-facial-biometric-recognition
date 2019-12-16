from django.shortcuts import redirect,render,get_object_or_404,HttpResponse
from django.contrib.auth import login
from django.contrib import auth
from Receptionist.models import *
def signin(request):
    if request.method =="POST":
        upassword  = request.POST["psw"]
        uname = request.POST["name"]
        ruser = auth.authenticate(username = uname, password =  upassword)
        receptionists = Receptionist.objects.all()
        print(ruser)
        required = 0
        for receptionist in receptionists:
            if receptionist.user == ruser:
                required = receptionist
                break
        if ruser and required: 
            auth.login(request,ruser)
            return redirect(home)
        

    
    return render(request, "signin.html")
def home(request):
    if request.method  == "POST":
        if request.POST["name"]:
            report =  Donation_Record()
            report.Name =  request.POST["name"]
            report.age = request.POST["age"]
            report.cnic = request.POST["cnic"]
            report.email = request.POST["email"]
            report.phone = request.POST["phone"]
            report.status = "Pending"
            report.save()
    return render(request, "home.html")