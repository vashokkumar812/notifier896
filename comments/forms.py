from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import post,comment

class postform(forms.Form): 
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
class commentform(forms.Form): 
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))