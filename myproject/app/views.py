from django.shortcuts import render, redirect
from django.http import HttpResponse
from app. models import *
from django.contrib.auth.hashers import make_password

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        email = request.POST['email']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])

        if Persone.objects.filter(email = email).exists():
            return HttpResponse("Email already register")
        elif Persone.objects.filter(phone=phone).exists():
            return HttpResponse("Phone already exists")
        else:
            Persone.objects.create(email=email, phone=phone,password=password)
            return HttpResponse("User Created")


def data(request):
    user = Persone.objects.all()
    return render(request, "table.html", {"user":user})

def user_delete(request,pk):
    Persone.objects.get(id=pk).delete()
    return redirect("/table/")

def update_user(request,uid):
    User_obj = Persone.objects.get(id=uid)
    return render(request, "update.html",{"User_obj":User_obj})

def update_view(request):
    if request.method == "POST":
        uid = request.POST.get('uid')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Persone.objects.filter(id=uid).update(email=email,phone=phone)
        return redirect("/table/")




