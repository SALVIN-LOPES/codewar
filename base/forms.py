from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Submission, User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(ModelForm):
    class Meta:
        model = User 
        fields = '__all__'   
        
class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['details']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','name','password1','password2']

