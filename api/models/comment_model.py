from django.db import models
from .base import Base
from .issue_model import IssueModel
from django.contrib.auth.models import User

class CommentModel(Base):
    body = models.TextField(
        help_text='Conteudo do Comentario',
        blank=False,
        null=False
    )
    issue = models.ForeignKey(
        IssueModel,
        on_delete=models.CASCADE,
        help_text='Issue qual percente ao comentario',
        related_name='comments'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        help_text='User qual percente ao comentario'
    )

    def __str__(self):
        description = f'Comentario de {self.user.username} em {self.issue.title}'
        return description