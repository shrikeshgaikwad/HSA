from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from app1.models import * 
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home (request):
    return render (request, "index.html")



def signup (request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        Sname = data.get('name')
        mob = data.get('mob')
        password = data.get('password')
        std = data.get('std')
        user = User.objects.create(
            username = username,
            first_name= Sname,
            mob = mob,         
        )
        user.set_password(password)
        user.save()

        student = Students.objects.create(
            user= user,
            Sname = Sname,
            username= username,
            std = std,
            mob = mob,
        )
        messages.info(request,'Account Created successfully')
        fees = Fees.objects.create(
            user=user,
            username = username,         
        )

        return redirect ('/signup/')
    return render (request,"signup.html")



def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        print(data)
        if not (User.objects.filter(username=username).exists()):
            messages.error(request,'INVALID USERNAME')
            return redirect ('/login/')

        user = authenticate(username = username,password = password)
        if user is None :
            messages.error(request,'INVALID PASSWORD')
            print(user)
            return redirect ('/login/')
        else:
            login(request,user)
            return redirect ('/studentProfile/')
    return render (request, "login.html")

@login_required
def studentProfile (request):
    if request.user.is_superuser:
        profile = Students.objects.all()
        fees = Fees.objects.all()
        return render (request, "adminpage.html",{'profile':profile,'fees':fees})

    else:
        profile = Students.objects.filter(user=request.user)
        fees = Fees.objects.filter(user=request.user)
        return render (request, "studentProfile.html",{'profile':profile,'fees':fees})

