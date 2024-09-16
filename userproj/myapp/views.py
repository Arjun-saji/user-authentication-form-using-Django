from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.models import User
from .import views

# def index(request):
#   if request.method=='POST':
#       username=request.POST['username']
#       password=request.POST['password']

#       user=authenticate(username=username,password=password)
#       if user is not None:
#           login(request,user)
#           return redirect("home.html")
#       else:
#           return render(request,"index.html")
#   else:
#       return render(request,"index.html")


#   return render(request,"index.html")


def home(request):
    return render(request,"home.html")

def signup(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        User.objects.create_user(username=username,password=password)
        print("ok")
        return redirect('home')
    return render(request,"index.html")

def logout(request):
    if request.method=='POST':
        logout(request)
        return redirect('index1.html') 
    return render(request,'home.html') 

def login(request):
    if request.method == "POST":
        username = request.POST.get('username1')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            #messages.success(request, 'You have been logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'index.html')
    # if request.method=="POST":
    #     username=request.POST.get('username')
    #     password=request.POST.get('password')
    #     user=authenticate(request,username=username,password=password)
    #     if user is not None:
    #         auth_login(request,user)
    #         return redirect('home')
    # return render(request,'login.html')



