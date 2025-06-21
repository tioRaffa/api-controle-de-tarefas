from django.urls import path
from rest_framework.routers import SimpleRouter
from api import views

router = SimpleRouter()
router.register('projects', views.ProjectListApiView, basename='project-api')
router.register('issues', views.IssueViewSet, basename='issues-api')


urlpatterns = []
urlpatterns += router.urls