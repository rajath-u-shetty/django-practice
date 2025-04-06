from django.shortcuts import render
from django.http import HttpResponse
from .models import variety

# Create your views here.
def chaiHome(request):
    chais = variety.objects.all()
    return render(request, 'chail.html',{"chai": chais})
