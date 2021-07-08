from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    # return HttpResponse('Hello World!, 안녕하세요!')
    if request.method == "POST":
        str = request.POST.get('hello_world_input')
        hello_world = HelloWorld()
        hello_world.text = str
        hello_world.save()      #save to DB

        hello_world_list = HelloWorld.objects.all()
        # return render(request, 'accountapp/hello_world.html', context={'text': str})
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        # Post 후 Get 방식으로 변경한다.
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        # return render(request, 'accountapp/hello_world.html', context={'text': str})
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
