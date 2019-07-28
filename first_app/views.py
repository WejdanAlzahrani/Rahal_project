<<<<<<< HEAD
from django.shortcuts import render ,reverse
from django.http import  HttpResponseRedirect
from .form import ContactForm
from django.contrib import messages 


def contact(request):
    form=ContactForm()
    if request.method=='POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data ['email']
            body=form.cleaned_data['body']
            messages.success(request,'Thank you')
            return HttpResponseRedirect(reverse('contact'))

    data={
        'form':form
    }
    return render(request,'contact.html',data)













=======
from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render (request, 'about.html')
>>>>>>> 85d5f9c90c42f21214535c4d7cd939c8bdcd876d




