from django.shortcuts import render
from . models import HouseOwner
# Create your views here.



def index(request):

    return render(request, 'hackhouse/base.html')


# def register(request):
#     if(request.method == )

