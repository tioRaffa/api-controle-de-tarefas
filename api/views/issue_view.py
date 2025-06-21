from rest_framework import viewsets, permissions
from api.permission import IsOwnerOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filter import IssueFilter

from api.models import IssueModel
from api.serializer import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = IssueModel.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    ]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = IssueFilter
    filterset_fields = [
        'status', 'priority', 'project', 'assignee', 'created_at'
    ]
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'status', 'priority', 'created_at']
    ordering = ['-id']


    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('project', 'reporter', 'assignee')
        return qs