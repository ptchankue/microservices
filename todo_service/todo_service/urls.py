from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework.urlpatterns import format_suffix_patterns


from todo_app.views import TodoViewSet

creation = TodoViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

details = TodoViewSet.as_view({
    'put': 'update',
    'get': 'retrieve',
    'delete': 'destroy'
})

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'todo_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # to create and show the list of todo for a particular user
    url(r'^api/v1/todos/$', creation, name='todo-creation'),

    # to update, view and delete a todo task
    url(r'^api/v1/todos/(?P<pk>[^/])/$', details, name='todo-detail'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)
