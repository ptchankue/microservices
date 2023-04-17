"""
    urls.py
    Defining endpoints
"""

from django.urls import path

from .views import SignUpViewSet, LoginViewSet, VerifyViewSet, home

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

    path('signup', signup, name='signup'),

    path('login', login, name='login'),

    path('users/<int:pk>', details, name='details'),

    path('verify', verify, name='verify-token'),

    path('validate', verify, name='validate-token'),

]

