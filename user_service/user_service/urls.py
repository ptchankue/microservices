"""
    urls.py
    Defining endpoints
"""
from django.conf.urls import include

from django.contrib import admin
from django.urls import path


admin.autodiscover()
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('api/v1/', include('user_app.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
