from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from rest_framework.urlpatterns import format_suffix_patterns


from user_app.views import (
    SignUpViewSet,
    LoginViewSet,
    VerifyViewSet
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

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'user_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/signup/$', signup, name='signup'),

    url(r'^api/v1/login/$', login, name='login'),

    url(r'^api/v1/verify/$', verify, name='verify-token'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)
