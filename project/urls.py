from django.urls import path
from .views import home as ProjectHome

urlpatterns = [
    path('', ProjectHome, name='project-home'),
]