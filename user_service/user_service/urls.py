from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from rest_framework.urlpatterns import format_suffix_patterns


from user_app.views import SignUpView

signup = SignUpView.as_view({
    'post': 'create'
})
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'user_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/signup/$', signup, name='home'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)
