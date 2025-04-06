from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chaiHome(request):
    return render(request, 'chail.html', name='chai home')

def order(request):
    return HttpResponse("order confirm")