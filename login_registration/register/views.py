from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def register(response):
    if response.method=='POST':
        form=RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form=RegisterForm()
    context={
        'form':form
    }
    return render(response,"register/register.html",context)

def logoutPage(request):
    return render(request,"registration/logout.html")

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
    return render(request,"registration/login.html")