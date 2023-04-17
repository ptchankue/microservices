"""
    urls.py
    Defining endpoints
"""
from django.conf.urls import include, path

from django.contrib import admin

from user_service.user_app.views import SignUpViewSet, LoginViewSet, VerifyViewSet, home

admin.autodiscover()
from rest_framework.urlpatterns import format_suffix_patterns




signup = SignUpViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

login = LoginViewSet.as_view({
    'post': 'create',
    #'get': 'list'
})

verify = VerifyViewSet.as_view({
    'post': 'create',
})

details = SignUpViewSet.as_view({
    'put': 'update',
    'get': 'retrieve',
    'delete': 'destroy'
})

urlpatterns = [
    path('', home, name='home'),

    path('api/v1/signup/', signup, name='signup'),

    path('api/v1/login/', login, name='login'),

    path('api/v1/users/(?P<pk>[^/])/', details, name='details'),

    path('api/v1/verify/', verify, name='verify-token'),

    path('api/v1/validate/', verify, name='validate-token'),

    path('admin/', include(admin.site.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
