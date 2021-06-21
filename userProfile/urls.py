from django.urls import path
from . import views
app_name="profile"
urlpatterns=[
    path('interest/',views.first_login,name='interest'),
    path('<str:username>/',views.profile,name="profile"),
]