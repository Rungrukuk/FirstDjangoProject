from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse("<h1>tech with kamal</h1>")
# Create your views here.


def v1(response):
    return HttpResponse("<h1>teze sayt?</h1>")
