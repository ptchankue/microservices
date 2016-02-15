from django.shortcuts import render, HttpResponse

from todo_app.models import Todo

from todo_app.serializers import TodoSerializer
# Create your views here.


def home(request):
    msg = "You have landed on the Todo service :)"
    return HttpResponse(msg)
class TodoViewSet(viewsets.ModelViewSet):

    """API endpoing to manage todo lists"""

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def create(self, request):
        pass

    def update(self, request):
        pass

    def retrieve(self, request):
        pass

    def destroy(self, request):
        pass
        
