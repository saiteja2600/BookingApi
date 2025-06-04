from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Home(request):
    
    return render(request, 'FrontEnd/index.html')

def login(request):
    
    return render(request, 'FrontEnd/login.html')

def signup(request):
    
    return render(request, 'FrontEnd/signup.html')

def bookSlot(request):
    
    return render(request, 'FrontEnd/bookslot.html')