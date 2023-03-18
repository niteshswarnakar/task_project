from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.get_home, name = "home-route"),
    path("todos/",views.get_todo,name = 'get-todo')
]                  