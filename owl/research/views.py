from django.shortcuts import render
from django.http import HttpResponse
# from .models import 


def index(request):
    return HttpResponse("Hello, world. You're at the research index.")


def detail(request, project_id):
    return HttpResponse("You're looking at project %s" % project_id)
