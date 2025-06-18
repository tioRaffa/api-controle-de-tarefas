from django.db import models
from .base import Base
from django.contrib.auth.models import User
from .project_model import ProjectModel


class IssueModel(Base):
    class Status(models.Choices):
        PENDING = 'PENDENTE', 'Pendente'
        IN_PROGRESS = 'EM_ANDAMENTO', 'Em Andamento'
        DONE = 'CONCLUIDO', 'Concluído'

    class Priority(models.Choices):
        LOW = 'BAIXA', 'Baixa'
        MEDIUM = 'MEDIA', 'Média'
        HIGH = 'ALTA', 'Alta'

    title = models.CharField(max_length=500, help_text='Titulo da Issue', blank=False, null=False)
    description = models.TextField(help_text='Descrição detalhada da Issue', blank=False, null=False)
    project = models.ForeignKey(
        ProjectModel,
        related_name='issues',
        on_delete=models.CASCADE,
        help_text="Projeto ao qual a issue pertence"
        )
    reporter = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        help_text='usuário que reportou a tarefa'
    )
    assignee = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text='suário responsável por resolver a Issue'
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        help_text='Status da Issue',
        blank=False,
        null=False
    )
    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.MEDIUM,
        help_text='Prioridade da Issue',
        blank=False,
        null=False
    )

    def __str__(self):
        return self.title
