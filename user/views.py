from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import login as login_user
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from .models import CustomUser

next = None

def login(request):
    global next
    loginForm = LoginForm()
    generalError = ""

    if(request.method == "GET"):
        next = request.GET.get("next")

    if(request.method == "POST"):
        loginForm = LoginForm(request.POST)
        if(loginForm.is_valid()):
            email = loginForm.cleaned_data.get("email")
            password = loginForm.cleaned_data.get("password")
            user = CustomUser.objects.filter(email=email).first()
            if(user is not None and check_password(password,user.password)):
                    print(next)
                    red = redirect("/")
                    login_user(request,user)
                    if(next != None):
                        red = redirect(next)
                        next = None
                    return red
            else:
                generalError = "მომხმარებელი ასეთი მონაცემებით არ მოიძებნა"
    return render(request,"user/login.html",{"form":loginForm,"generalError":generalError})

def register(request):
    if(request.method == "POST"):
        userForm = RegistrationForm(request.POST)
        if(userForm.is_valid()):
            data = userForm.cleaned_data
            user = CustomUser.objects.create_user(
                email = data["email"],
                password = data["password"],
                phone = data["phone"],
                fullname = data["fullname"]
            )
            login_user(request,user)
            return redirect("/")
        else:
            return render(request,"user/register.html",{"form":userForm})
    return render(request,"user/register.html",{})

@login_required(login_url="/user/login")
def dashboard(request):
    return render(request,"user/dashboard.html",{"user":request.user})

def logout(request):
    logout_user(request)
    return redirect("/")