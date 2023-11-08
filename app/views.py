from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sree(request):
    return HttpResponse('<h1>Hello Sree</h1>')

def siva(request):
    return HttpResponse('<marquee><h1 style="color:red"> Hai Raa Gundu Siva ..</h1></marquee>')