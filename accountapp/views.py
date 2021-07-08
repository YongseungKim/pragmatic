from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    # return HttpResponse('Hello World!, 안녕하세요!')
    if request.method == "POST":
        str = request.POST.get('hello_world_input')
        hello_world = HelloWorld()
        hello_world.text = str
        hello_world.save()      #save to DB
        # return render(request, 'accountapp/hello_world.html', context={'text': str})
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': hello_world})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': str})
