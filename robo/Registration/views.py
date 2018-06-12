from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import personal
import numpy as np



# Create your views here.

def home(request):

    return render(request, 'register/home.html', {})

def signup(request):

    #import smtplib
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.login("santhosh92.mca@gmail.com", "qwerty619")
    #msg = " python mail checking process"
    #server.sendmail("santhosh92.mca@gmail.com", "santhosh92.mca@.com", msg)

    a = personal.objects.all()
    name=[]
    address=""
    for i in a:    	
    	if i.Age == 22:    		
    		name.append(lambda: i.name)
    		print(i.name,i.Address)

    print([f() for f in name])
    print(name)
    return render(request, 'register/signup.html', {"name":name})

def contact_us(request):
    return render(request, 'register/contact_us.html', {})