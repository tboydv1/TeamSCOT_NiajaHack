from django.contrib.auth import authenticate, login, logout,
from django.shortcuts import render, redirect
from . models import HouseOwner
from django.contrib.auth.forms import 
# Create your views here.



def index(request):

    return render(request, 'hackhouse/Landing.html')


def register(request):
    if(request.method == 'POST'):
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']


        newUser = HouseOwner(firstname = first_name, lastname = last_name, email= email,
                             username = username, password = password)
        newUser.save()

        return redirect("/hackhouse/successful")
    else:
        return render(request, 'hackhouse/register.html')

def success(request):
    return render(request, "hackhouse/Congrats.html")

def user_login(request):
    if request.method == 'POST'
        form = Use
