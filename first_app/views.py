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

















