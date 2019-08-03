from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, blogForm, loginForm, userForm, profileForm
from .models import blog, profile
from django.contrib import messages
from rest_framework import viewsets
from .serializers import blogSerializer , profileSerializer

def home(request):
    blog_obj=blog.objects.all()
    data = {'blog':blog_obj}
    return render(request, "index.html", data)


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
    form=blogForm()
    if request.method=='POST':
        form=blogForm(request.POST)
        if form.is_valid():
            blog=form.save(commit=False)
            if 'picture' in request.FILES:
                blog.picture=request.FILES['picture']
            blog.blogger=request.user
            blog.save()
            messages.success(request,'your blog added successfully')
            return HttpResponseRedirect(reverse('home'))
    data={'form':form}
    return render(request,'add_blog.html',data)


def login_user(request):
    form=loginForm()

    if request.method =="POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user :
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.error(request, 'your account is blocked')
            else:
                messages.error(request, 'invalid username or password')
    data={'form':form}

    return render(request,'login.html',data)


def register(request):
    loginForm_obj=loginForm()
    userForm_obj=userForm()
    profileForm_obj=profileForm()

    if request.method=="POST":
        loginForm_obj=loginForm(request.POST)
        userForm_obj=userForm(request.POST)
        profileForm_obj=profileForm(request.POST)

        if userForm_obj.is_valid() and profileForm_obj.is_valid() and loginForm_obj.is_valid():
            user=userForm_obj.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile=profileForm_obj.save(commit=False)
            profile.user=user
            profile.save()

            username = loginForm_obj.cleaned_data['username']
            password = loginForm_obj.cleaned_data['password']

            user = authenticate(username=username, password=password)
            login(request, user)
            
            return HttpResponseRedirect(reverse('home'))

    data={'userForm':userForm_obj,'profileForm':profileForm_obj}
    return render(request,'register.html',data)

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def blogDetails(request,pk):
    blog_obj=blog.objects.get(pk=pk)
    readers=int(blog_obj.readers)
    readers+=1
    blog_obj.readers=readers
    blog_obj.save()
    data={'blog':blog_obj}
    return render(request,'blogDetails.html',data)
  
@login_required
def userProfile(request,pk):
    user = User.objects.get(pk=pk)
    blogs=blog.objects.filter(blogger=user)
    profile_obj=profile.objects.get(user=user)
    data={'profile':profile_obj,'blogs':blogs}
    return render(request,'profile.html',data)

class blogViewSet(viewsets.ModelViewSet):
    queryset=blog.objects.all()
    serializer_class=blogSerializer


class profileViewSet(viewsets.ModelViewSet):
    queryset=profile.objects.all()
    serializer_class=profileSerializer
