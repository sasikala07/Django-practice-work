from.views import loginpage
from.views import registerpge,contactpage
from django.urls import path


urlpatterns = [
     path('login',loginpage),  ##loginpage is the func in the views.py
     path('signup',registerpge),
     path('contact',contactpage)
]
