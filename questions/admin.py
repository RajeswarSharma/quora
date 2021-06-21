from django.contrib import admin
from .models import Questions,Comments,Replies
# Register your models here.
admin.site.register(Questions)
admin.site.register(Comments)
admin.site.register(Replies)