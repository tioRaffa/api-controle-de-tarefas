from rest_framework import viewsets, permissions
from api.permission import IsOwnerOrReadOnly

from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filter import IssueFilter

from api.models import IssueModel, CommentModel
from api.serializer import IssueSerializer, CommentSerializer


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
    
    @action(detail=True, methods=['get', 'post'])
    def comments(self, request, pk=None):
        issue = self.get_object()

        if request.method == 'GET':
            comments = issue.comments.all().select_related('user').order_by('-id')
            page = self.paginate_queryset(comments)
            if page is not None:
                serializier = CommentSerializer(page, many=True, context={'request': request})
                return self.get_paginated_response(serializier.data)
            
            serializier = CommentSerializer(comments, many=True, context={'request': request})
            return Response(serializier.data)
        
        if request.method == 'POST':
            data = request.data.copy()
            data['issue_id'] = issue.pk

            serializier = CommentSerializer(data=data, context={'request':request})
            serializier.is_valid(raise_exception=True)
            serializier.save(user=request.user)
            return Response(serializier.data, status=201)