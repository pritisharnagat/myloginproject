from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import Forms
from.forms import HomeForm
# Create your views here.
def home(request):
    return render(request,'users/home.html')


def register(request):
    if request.method=="POST":
        form=HomeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"your account has been created.you can log in now!")
            return redirect("login")
    else:
        form=HomeForm()
    context={"form":form}        
    return render(request,"users/register.html",context) 

