from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView


# Create your views here.
def registerView(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password12 = request.POST.get("password12")

        if(password1 == password12):
            user = authenticate(username=name,email=email,password=password1)

            if(user == None):
                user = User.objects.create_user(username=name,email=email,password=password1)
                login(request,user)
                return redirect(reverse("home"))
            else:
                return render(request,"account/error.html")
        else:
            return render(request,"account/error.html")
    else:
        return render(request,"account/error.html")
            
        

def loginView(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=name,email=email,password=password)

        if(user != None):
            login(request,user)
            return redirect(reverse("home"))
        else:
            return render(request,"account/error.html")

def logoutView(request):
    logout(request)
    return redirect(reverse("home"))

