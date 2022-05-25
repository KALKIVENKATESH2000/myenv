from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return render(request, "index.html")

def demo(request):
    return HttpResponse("this is demo responsce")