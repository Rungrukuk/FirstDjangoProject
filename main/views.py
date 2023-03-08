from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    return render(response, "main/base.html", {"ls": ls})


def home(response):
    return render(response, "main/home.html", {})


def list(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls": ls})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            t = ToDoList(name=form.cleaned_data["name"])
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})
