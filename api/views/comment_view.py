from rest_framework import viewsets, permissions
from api.permission import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from api.models import CommentModel
from api.serializer import CommentSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

class CommentView(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['issue'] # GET /api/v1/comments/?issue=id

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('issue', 'user')
        return qs.order_by('-id')

    @action(detail=False, methods=['get'], url_name='me')
    def my_comments(self, request):
        user = request.user

        comments = self.get_queryset().filter(user=user)
        page = self.paginate_queryset(comments)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)


