from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import auth
from django.contrib import messages
from questions.models import Questions
from django.urls import reverse
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.profile.first_login == True:
            return redirect(reverse('profile:interest'))
        tags = request.user.profile.following.names()
        questions = Questions.objects.filter(tags__name__in=tags).distinct()
        return render(request,'home/home.html',{'questions':questions})

    else:
        return redirect('accounts:login')

def logout(request):
    auth.logout(request)
    messages.info(request,"Logged out successfully")
    return redirect(reverse('accounts:login'))
