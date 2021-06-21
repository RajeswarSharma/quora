from django.urls import path
from . import views
app_name="questions"
urlpatterns=[
    path('add-question/',views.add_question,name='add_question'),
    path('<int:id>/',views.question_details,name="question_details"),
    path('topic/<str:tag>/',views.topic_space,name="topic")
]