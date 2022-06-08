from urllib import response
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello</h1>")

def about(request):
    return HttpResponse("<h1>This is about us.</h1>")

def contact(request):
    return HttpResponse("<h1>This is how you can reach us.</h1>")

def services(request):
    return HttpResponse("<h1>These are the services we provide.</h1>")