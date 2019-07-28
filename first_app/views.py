from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data={}
    return render(request, 'home.html',data)


def about(request):
    return render (request, 'about.html')




