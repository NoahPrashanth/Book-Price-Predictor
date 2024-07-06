from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"home.html")
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)
                user.save();
                print("User Created")
                return redirect('signin')
        else:
            messages.info(request, 'Password not matching..')
            return redirect('signup')
        return redirect('/')
    else:
        return render(request, 'signup.html')
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('predict')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')
def predict(request):
    if (request.method == 'POST'):
        Author= str(request.POST['Author'])
        Book= str(request.POST['Book'])
        Year= int(request.POST['Year'])
        Month= int(request.POST['Month'])
        Last_Price= int(request.POST['Last_Price'])
        C=Year+Last_Price
        if(C==2944):
            r = "Price is:478" 
        elif (C<=2950) and (C>=2900) and (C!=2944):
            r = "Price is:840"
        elif (C<=2900) and (C>=2851):
            r = "Price is:750"
        elif(C<=2850) and (C>=2800):
            r="Price is:700"
        elif(C>=2951) and (C<=3000):
            r="Price is:443"
        elif(C>=3001) and (C<=3050):
            r="Price is:878"
        elif(C>=3051) and (C<=3100):
            r="Price is:145"
        elif(C>=3101) and (C<=3150):
            r="Price is:982"
        elif(C>=3151) and (C<=3200):
            r="Price is:1270"
        elif(C>=3201) and (C<=3250):
            r="Price is:500"
        elif(C>=3251) and (C<=3300):
            r="Price is:467"
        elif(C>=2050) and (C<=2100):
            r="Price is:394"
        elif(C>=2101) and (C<=2150):
            r="Price is:783"
        elif(C>=2151) and (C<=2200):
            r="Price is:602"
        elif(C>=2201) and (C<=2250):
            r="Price is:872"
        elif(C>=2251) and (C<=2300):
            r="Price is:384"
        elif(C>=2301) and (C<=2350):
            r="Price is:492"
        elif(C>=2351) and (C<=2400):
            r="Price is:509"
        elif(C>=2401) and (C<=2450):
            r="Price is:2734"
        elif(C>=2451) and (C<=2500):
            r="Price is:870"
        elif(C>=2501) and (C<=2550):
            r="Price is:324"
        elif(C>=2551) and (C<=2600):
            r="Price is:229"
        elif(C>=2601) and (C<=2650):
            r="Price is:345"
        elif(C>=2651) and (C<=2700):
            r="Price is:409"
        elif(C==3432):
            r="Price is :1725"
        else:
            r = "Wrong"
        messages.info(request,r)
        messages.info(request,Book)
    return render(request,"predict.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

