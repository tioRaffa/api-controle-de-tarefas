from rest_framework import serializers

from api.models import IssueModel, ProjectModel
from django.contrib.auth.models import User

from .project_serializer import ProjectSerializer
from djoser.serializers import UserSerializer


class IssueSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request', None)
        if request and not request.user.is_anonymous:
            self.fields['project_id'].queryset = ProjectModel.objects.filter(owner=request.user)


    project = ProjectSerializer(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(
        queryset = ProjectModel.objects.all(),
        source='project',
        write_only=True,
        required=True
    )
    reporter = UserSerializer(read_only=True)
    assignee = UserSerializer(read_only=True) # -> INFO DO RESPONSAVEL POR RESOLVER A TASK | GET 
    assignee_id = serializers.PrimaryKeyRelatedField( # -> ID DO RESPONSAVEL POR RESOLVER A TASK | POST_PATCH 
        queryset=User.objects.all(),
        source='assignee',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = IssueModel
        fields = [
            'id',
            'title',
            'description',
            'project',
            'project_id',
            'reporter',
            'assignee',
            'assignee_id',
            'status',
            'priority',
        ]

    def validate(self, data):
        assignee = data.get('assignee')
        reporter = self.context['request'].user if self.context.get('request') else None

        if assignee and reporter and assignee == reporter:
            raise serializers.ValidationError(
                {"assignee_id": "O responsável (assignee) não pode ser a mesma pessoa que reportou a issue."}
            )
        return data