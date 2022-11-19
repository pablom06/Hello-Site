from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View 


class HelloWorldView(View):
    def get(self, request):
        return render(request, template_name='hello_world.html')

class HelloView(View):
    def get(self, request, name):
        return render(request, template_name='hello_name.html',
        context = {'person': name},
        )