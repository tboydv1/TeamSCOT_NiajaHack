from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import HouseOwner
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Create your views here.



def index(request):
    return render(request, 'hackhouse/index.html')

def contact(request):
    return render(request, 'hackhouse/contact.html')

def about(request):
    return render(request, 'hackhouse/about.html')


def register(request):

    if(request.method == 'POST'):

        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(first_name = first_name,last_name=last_name,username=username, email= email, password=password)
        user.save()

        # newUser = HouseOwner(firstname = first_name, lastname = last_name, email= email,
        #                      username = username, password = password)
        # newUser.save()

        return redirect("/hackhouse/successful")
    else:
        return render(request, 'hackhouse/register.html')

def success(request):
    return render(request, "hackhouse/Congrats.html")




def user_login(request):




    if request.method == 'POST':

        user_name = request.POST['username']
        pass_word = request.POST['password']

        user = authenticate(username=user_name, password=pass_word)

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            if user is not None:
                login(request, user)
                # messages.error(request, f"You are now logged in as {username}")
                return render(request, 'hackhouse/home.html', {'user':user})
            # else:
            #     messages.error(request, "Invalid username or password")
        else:
            return HttpResponse("User login not valid")
    else:
        form = AuthenticationForm()
        return render(request= request, template_name='hackhouse/loginPage.html', context={"form":form})