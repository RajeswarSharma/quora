from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username is already taken")
            return redirect('accounts:register')
        if User.objects.filter(email = email).exists():
            messages.info(request,"Email is already registered")
            return redirect('accounts:register')
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,email=email,password = password)
        user.save()
        return redirect('accounts:login')
    else:
        return render(request,'accounts/register.html')

    
def login(request):
    if request.user.is_authenticated==False:    
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.info(request,'Incorrect username or password')
                return redirect('accounts:login')

        return render(request,'accounts/login.html')
    else:
        return redirect('/')
