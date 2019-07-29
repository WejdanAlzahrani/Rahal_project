from django import forms
from .models import blog


class ContactForm(forms.Form) :
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    body=forms.CharField (widget=forms.Textarea)


class blogForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    class Meta:
        model = blog
        fields = ['title', 'Type', 'content', 'picture']

        
       

       
