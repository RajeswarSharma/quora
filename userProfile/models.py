from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from taggit.managers import TaggableManager
from taggit.models import Tag
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=150)
    first_login = models.BooleanField(default=True)
    following = TaggableManager()

    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
