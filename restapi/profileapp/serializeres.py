from rest_framework import serializers
from .models import Profile

class ProfileSerializer (serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields= '__all__'  ##serialize all content into json ..py obj to json

