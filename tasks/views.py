from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from tasks.models import Task
from tasks.serializer import Serializer


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(["GET"])
def get_all_tasks(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = Serializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(["POST"])
def post_task(request):    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
'''
def put_task(request):    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
'''
@api_view(["DELETE"])
def delete_tasks(request):    
    if request.method == 'DELETE':
        task = Task.objects.all().delete()
        return JsonResponse({"status": 200, "message": "Tasks deleted"}, status=200)
