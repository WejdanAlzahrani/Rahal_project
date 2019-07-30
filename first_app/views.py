from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm, blogForm
from .models import blog
from django.contrib import messages


def home(request):
    blog_obj=blog.objects.all()
    data = {'blog':blog_obj}
    return render(request, "home.html", data)


def about(request):
    return render(request, "about.html")


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            body = form.cleaned_data["body"]
            messages.success(request, "Thank you")
            return HttpResponseRedirect(reverse("contact"))

    data = {"form": form}
    return render(request, "contact.html", data)


def add(request):
    form = blogForm()
    if request.method == "POST":
	    form = blogForm(request.POST)
	    if form.is_valid():
	        blog = form.save(commit=False)
	        if 'picture' in request.FILES:
	            blog.picture = request.FILES['picture']
	            blog.save()            
	            messages.success(request, 'your Blog have been added succesfully')
	        return HttpResponseRedirect(reverse('home'))
    data ={'form': form}
    return render(request, 'add_blog.html', data)