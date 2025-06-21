from rest_framework import viewsets, permissions
from api.permission import IsOwnerOrReadOnly

from api.models import CommentModel
from api.serializer import CommentSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    ]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('issue', 'user')
        return qs.order_by('-id')


