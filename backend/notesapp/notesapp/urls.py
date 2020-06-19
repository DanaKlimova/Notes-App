from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    re_path(r'api/v1/', include('notes.urls')),
    path('admin/', admin.site.urls),
]
