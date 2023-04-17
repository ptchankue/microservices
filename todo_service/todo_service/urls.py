from django.conf.urls import include

from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/v1/', include('todo_app.urls')),
    path('admin', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
