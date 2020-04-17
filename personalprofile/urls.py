from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('resume.urls')),
    path('project/', include('project.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
