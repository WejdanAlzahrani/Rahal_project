from django import forms
from .models import blog, profile
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)


class blogForm(forms.ModelForm):
	    picture = forms.ImageField(required=False)
	    class Meta:
	        model = blog
	        fields = ['title', 'Type','country', 'content', 'picture']


class loginForm(forms.Form):
    username=forms.CharField(max_length=150)
    password=forms.CharField(widget=forms.PasswordInput)


class userForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']


class profileForm(forms.ModelForm):
    
    class Meta:
        model = profile
        fields = ['mobile','gender']

