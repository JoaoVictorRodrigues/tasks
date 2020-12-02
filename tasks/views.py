from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from tasks.models import Task
from tasks.serializer import Serializer


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@csrf_exempt
def get_all_tasks(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = Serializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

def post_task(request):    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
