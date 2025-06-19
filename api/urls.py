from django.urls import path
from rest_framework.routers import SimpleRouter
from api import views

router_projects = SimpleRouter()
router_projects.register(
    'projects',
    views.ProjectListApiView,
    basename='projects-api'
)

urlpatterns = [
    
]

urlpatterns += router_projects.urls