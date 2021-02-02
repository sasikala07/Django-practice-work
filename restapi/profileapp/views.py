from django.shortcuts import render
from .models import Profile
# Create your views here.
from rest_framework.decorators import APIView
from rest_framework.response import Response
from.serializeres import ProfileSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_201_CREATED
##class based view

class ProfileDetailView(APIView):
    def get(self,request,id):
     try:
            prof=Profile.objects.get(id=id)
            serializer=ProfileSerializer(prof)
            return Response(serializer.data)
     except:
            return Response("not found")

    def put(self,request,id): ##update the details
##put is similar to post ...only diff is here serialize the existing data also
        prof=Profile.objects.get(id=id)
        serializer=ProfileSerializer(prof,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("updated!!!!!")
        else:
            return Response(serializer.errors)

    def delete(self,request,id):
        prof=Profile.objects.get(id=id)
        prof.delete() ##deleted the particular data using id
        return Response("Deleted!!!")



class ProfileListView (APIView):

    def get (self, request):
        profiles= Profile.objects.all() #use django orm shell
        # serializer to convert py obj to json
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


    def post(self,request):
        #print(reques.data) ..show the profile details requested
        serializer=ProfileSerializer(data=request.data)
        if serializer.is_valid():  ##to check valid or not
            serializer.save()  ##save the new details ..post
            return Response("saved!!!",status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
