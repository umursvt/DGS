from django.shortcuts import render,redirect
from .forms import RegisterForm
from .forms import Login
from django.contrib.auth.models import User 
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            messages.success(request,"Başarıyla kayıt oldunuz.")

            login(request,newUser)
            return redirect("home")
        else:
            context={
                "form":form
            }
            return render(request,"uyelik/register.html",context)
    else:
        form= RegisterForm()
        context={
            "form":form
        }
        return render(request,"uyelik/register.html",context)
    



def loginUser(request):
    form= Login(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,'uyelik/login.html',context)
        messages.success(request,"Başarıyla Giriş Yapıldı.  ",)
        login(request,user)
        return redirect("home")
    return render(request,'uyelik/login.html',context)



def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yapıldı")
    return redirect('home')

def profil(request):
    return render(request,'uyelik/profil.html')

