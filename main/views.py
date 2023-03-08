from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    return render(response, "main/base.html", {"ls": ls})


def home(response):
    return render(response, "main/home.html", {})


def list(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls": ls})
# Create your views here.
