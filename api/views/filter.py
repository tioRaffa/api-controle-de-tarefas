import django_filters
from django.contrib.auth.models import User
from api.models import IssueModel, ProjectModel

class IssueFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    project = django_filters.ModelChoiceFilter(queryset=ProjectModel.objects.all())
    assignee = django_filters.ModelChoiceFilter(queryset=User.objects.all())

    created_at = django_filters.DateFilter(field_name='created_at__date')
    created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = IssueModel
        fields = {
            'status': ['exact'],
            'priority': ['exact'],
        }