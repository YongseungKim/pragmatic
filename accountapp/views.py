from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world(request):
    # return HttpResponse('Hello World!, 안녕하세요!')
    return render(request, 'accountapp/hello_world.html')
