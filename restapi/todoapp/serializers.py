from rest_framework.serializers import ModelSerializer
from .models import Task

class TaskSeralizer (ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"
