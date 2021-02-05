from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer, BookSerializer, PublisherSerializer,UserSerializer
from .models import Author,Publisher, Book
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User


# Create your views here.


class AuthorView (ModelViewSet):
   serializer_class = AuthorSerializer
   queryset = Author.objects.all()
##to get permission..authenticated users can only be acces thrugh using username paswd ..isauthenticated
   permission_classes = (IsAuthenticated,)

class PublisherView (ModelViewSet):
   serializer_class = PublisherSerializer
   queryset = Publisher.objects.all()
   permission_classes = (IsAuthenticated,)

class BookView (ModelViewSet):
   serializer_class = BookSerializer
   queryset = Book.objects.all()
   permission_classes = (IsAuthenticated,)

class UserCreater (CreateAPIView):
   serializer_class =UserSerializer
   queryset = User.objects.all()
##allowany ...is can be acces any of the users ...
   permission_classes = (AllowAny,)









