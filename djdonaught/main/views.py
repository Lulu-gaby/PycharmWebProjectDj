from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'main/index.html')
def facts(request):
    return render(request, 'main/facts.html')
def recipies(request):
    return render(request, 'main/recipies.html')
def photos(request):
    return render(request, 'main/photos.html')
def stories(request):
    return render(request, 'main/stories.html')