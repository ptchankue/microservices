"""
    urls.py
    Defining endpoints
"""
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from rest_framework.urlpatterns import format_suffix_patterns


from user_app.views import (
    SignUpViewSet,
    LoginViewSet,
    VerifyViewSet,
)

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

urlpatterns = patterns(
    '',

    url(r'^$', 'user_app.views.home', name='home'),

    url(r'^api/v1/signup/$', signup, name='signup'),

    url(r'^api/v1/login/$', login, name='login'),

    url(r'^api/v1/users/(?P<pk>[^/])/$', details, name='details'),

    url(r'^api/v1/verify/$', verify, name='verify-token'),

    url(r'^api/v1/validate/$', verify, name='validate-token'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)
