from rest_framework import serializers
from api.models import CommentModel, IssueModel

from djoser.serializers import UserSerializer
from .issue_serializer import IssueSerializer

class CommentSerializer(serializers.ModelSerializer):
    issue = serializers.HyperlinkedRelatedField(
        view_name='issue-api-detail',
        read_only=True
    )
    issue_id = serializers.PrimaryKeyRelatedField(
        queryset=IssueModel.objects.all(),
        source='issue',
        write_only=True

    )
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = CommentModel
        fields = [
            'id',
            'body',
            'issue',
            'issue_id',
            'user'
        ]
