from django.urls import path
from .views import home as BlogHome

urlpatterns = [
    path('', BlogHome, name='blog-home'),
]