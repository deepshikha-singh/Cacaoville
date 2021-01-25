from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import *

# Create your views here.
def index(request):
    Sliders = Slider.objects.all()
    return render(request, 'index.html', {'Sliders': Sliders})

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')

def contact(request):
    return render(request, 'contact-us.html')

def signup(request):
    if request.method == 'POST':
        # Get the post param eters
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        # Create New User
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Cacaoville account has been successfully created")
        return redirect('index')
    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        #Get the post parameter
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None: 
            auth_login(request, user)
            messages.success(request, "Sucessfully Login into Cacaoville")
            print("Logged in")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials!  Please try again")
            return redirect('signin')
    else:
        return render(request, 'signin.html')


    

