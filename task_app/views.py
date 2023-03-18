from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import Todo
from .serializers import TodoSerializer
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

def get_home(req):
    return JsonResponse("You have reached this route",safe=False)

@api_view(['GET'])
def get_todo(req):
    response_data = []
    todos = Todo.objects.all()
    serialized_data = TodoSerializer(todos, many = True)

    return Response(serialized_data.data)
    
    # return JsonResponse("something went wrong",safe=False)