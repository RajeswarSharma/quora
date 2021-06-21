from django.shortcuts import get_object_or_404, redirect, render
from taggit.models import Tag
from django.urls import reverse
import json
from django.contrib.auth.models import User
from questions.models import Questions,Comments
from django.utils import timezone

# Create your views here.

def first_login(request):
    if request.user.is_authenticated and request.user.profile.first_login == True:
        if request.method == "POST":
            tags = json.loads(request.POST["tags"])
            print(tags)
            for tag in tags:
                request.user.profile.following.add(tag)
            request.user.profile.first_login = False
            request.user.profile.save()
            return redirect(reverse("home:home"))
        else:
            tags = Tag.objects.all()
            if len(tags)>=50:
                l = list([str(tag) for tag in tags[50:]])
                json_optional_tags = json.dumps(l)
                return render(request,'userProfile/interest.html',{'tags':tags[:50],'json_optional_tags':json_optional_tags})
            return render(request, 'userProfile/interest.html', {'tags': tags})
    else:
        return redirect(reverse("accounts:login"))

def profile(request,username):
    user = get_object_or_404(User,username = username)
    if request.user.username == username:
        if request.method == "POST":
            request.user.profile.bio=request.POST['new-bio-tt']
            request.user.profile.save()
            return redirect(reverse("profile:profile", args=[request.user]))
        else:
            bio = user.profile.bio
            questions = Questions.objects.filter(author = user)
            answers = Comments.objects.filter(cmnt_author = user)
            following = user.profile.following.names()
            content={
                "user":user,
                "bio":bio,
                "questions":questions,
                "answers":answers,
                "following":following,
            }
            return render(request,"userProfile/profile.html",content)
    else:
        bio = user.profile.bio
        questions = Questions.objects.filter(author=user)
        answers = Comments.objects.filter(cmnt_author=user)
        following = user.profile.following.names()
        content = {
            "user": user,
            "bio": bio,
            "questions": questions,
            "answers": answers,
            "following": following,
        }
        return render(request, "userProfile/profile_notuser.html", content)
        #show details only 
    #if invalid username return 404
   
    

