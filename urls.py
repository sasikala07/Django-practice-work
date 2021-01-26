
from.views import loginpage  ##import the views of loginpage
from.views import registerpge  ##import the views registerpage
from django.urls import path


urlpatterns = [
     path('login',loginpage),  ##loginpage is the func in the views.py
     path('signup',registerpge)
]
