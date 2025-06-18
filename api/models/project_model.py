from django.db import models
from .base import Base
from django.contrib.auth.models import User

class ProjectModel(Base):
    title = models.CharField(max_length=50, help_text='Nome do Projeto')
    description = models.TextField(
        blank=True, 
        null=True, 
        help_text='Descrição detalhada do projeto'
        )
    owner = models.ForeignKey(
        User,
        related_name='owned_projects',
        help_text="Usuário que gerencia o projeto",
        on_delete=models.CASCADE
        )
    
    def __str__(self):
        return self.title

