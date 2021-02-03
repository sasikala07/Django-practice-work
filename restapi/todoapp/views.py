from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework import viewsets
from .serializers import TaskSeralizer
from .models import Task


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSeralizer  # add this
    queryset = Task.objects.all()

##if we want to update or get to create own code or regexp ,email appln in the existing code
    #we need to get the below code  from modelviewset ...viewset page..uodate own code
    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = TaskSeralizer(data=request.data)
        if serializer.is_valid():  ##check valid or not ...saved or not
            serializer.save()
            return Response("saved!!!", status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
