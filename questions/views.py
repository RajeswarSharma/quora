from taggit.models import Tag
from .models import Comments, Questions
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from taggit.utils import _parse_tags
from django.urls import reverse

# Create your views here.
def add_question(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            question_title = request.POST['question_title']
            question_text = request.POST['question_text']
            tags = _parse_tags(request.POST['tags'])
            question = Questions(question_title=question_title,question_text=question_text,author = request.user)
            question.save()
            for tag in tags:
                question.tags.add(tag)
            question.save()
            return redirect(reverse('questions:question_details',kwargs={'id':question.id}))
        else:
            return render(request,'questions/add_question.html')
    else: return redirect("/")

def question_details(request,id):
    question = get_object_or_404(Questions, pk=id)
    if request.method=='POST':
        
        if request.user.is_authenticated:
            if 'comment' in request.POST:
                comment_text = request.POST['comment_text']
                question.comments_set.create(comment_text=comment_text,cmnt_author = request.user)
            
            if 'reply' in request.POST:
                reply_text = request.POST['reply_text']
                comment = get_object_or_404(Comments,pk=int(request.POST['cmnt_id']))
                comment.replies_set.create(reply_text= reply_text,author=request.user)
                
            return redirect(reverse('questions:question_details',kwargs={'id':id}))
        
        else: return redirect('/')    
    return render(request,"questions/question_details.html",{'question':question})

def topic_space(request,tag):
    if request.method == "POST":
        if request.POST['btnf'] == "follow":
            request.user.profile.following.add(tag)
        elif request.POST['btnf']=='unfollow':
            request.user.profile.following.remove(tag)
    isfollowing = 0
    stat_tag = Tag.objects.filter(name=tag)
    if len(stat_tag)==0:
        return render(request,"questions/noresult.html")
    if tag in request.user.profile.following.names():
        isfollowing=1
    questions = Questions.objects.filter(tags__name__in=[tag]) 
    return render(request,"questions/topic.html",{'questions':questions,'tag':tag,'isfollowing':isfollowing})