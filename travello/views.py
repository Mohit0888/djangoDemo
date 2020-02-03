from django.shortcuts import render
from django.http import HttpResponse
from .models import Destinations
# Create your views here.
def index(request):

    dests= Destinations.objects.all()
    return render(request,'index.html' , {'dests' : dests})