from django.urls import path
from .views import project_home

urlpatterns = [
    path('', project_home, name='project-home'),
]