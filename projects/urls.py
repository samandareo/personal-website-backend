from django.urls import path
from .views import ProjectsAPIView, ProjectDetailAPIView

urlpatterns = [
    path('api/projects/', ProjectsAPIView.as_view(), name='projects-list'),
    path('api/projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail')
]