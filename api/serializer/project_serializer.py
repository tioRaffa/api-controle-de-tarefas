from rest_framework import serializers
from djoser.serializers import UserSerializer
from api.models import ProjectModel



class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = ProjectModel
        fields = [
            'id',
            'title',
            'description',
            'owner'
        ]