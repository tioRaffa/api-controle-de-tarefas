from rest_framework import viewsets, permissions
from api.permission import IsOwnerOrReadOnly

from api.models import ProjectModel
from api.serializer import ProjectSerializer, IssueSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

class ProjectListApiView(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['get'], url_name='issues-api')
    def list_project_issues(self, request, pk=None):
        project = self.get_object()
        issues_queryset = project.issues.all().order_by('-id')

        self.pagination_class.page_size = 2
        page = self.paginate_queryset(issues_queryset)
        if page is not None:
            serializer = IssueSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)
        
        serializer = IssueSerializer(issues_queryset, many=True, context={'request': request})
        return Response(serializer.data)
        