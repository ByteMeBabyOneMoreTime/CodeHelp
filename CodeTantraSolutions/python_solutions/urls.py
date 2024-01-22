from django.urls import path 
from . import views
urlpatterns = [
    path('python/', views.Answers, name="Answers")
]
