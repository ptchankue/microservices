from django.urls import path, include

from .views import TodoViewSet, home


creation = TodoViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

details = TodoViewSet.as_view({
    'put': 'update',
    'get': 'retrieve',
    'delete': 'destroy'
})


urlpatterns = [
    path('', home, name='home'),
    path('todos/', creation, name='todo-create'),
    # to update, view and delete a todo task
    path('todos/<int:pk>', details, name='todo-detail'),
]

