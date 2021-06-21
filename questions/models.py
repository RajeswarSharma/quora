from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from taggit.managers import TaggableManager
from django.utils import timezone
# Create your models here.

class Questions(models.Model):
    question_title = models.TextField(max_length=300,default="Default")
    question_text = models.TextField(max_length=500)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = TaggableManager()
    pub_date = models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return str(self.question_text)

class Comments(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=300)
    pub_date = models.DateTimeField(default=timezone.now)
    cmnt_author= models.ForeignKey(User,on_delete=models.CASCADE)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.comment_text)

class Replies(models.Model):
    reply_text = models.TextField(max_length=300)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(Comments,on_delete=models.CASCADE) 
    
    def __str__(self):
        return str(self.reply_text)
