from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('home')

def about(request):
    return render (request, 'about.html')

def login(request):
    return HttpResponse('login')


def contact(request):
    return HttpResponse('contact')