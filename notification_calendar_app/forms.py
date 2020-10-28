from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Task

# password1 and password2 are "custom" fields on the UserCreationForm since they do not exist as model fields on the User model. Meta.widgets will not work for these custom fields, you will need to redefine these fields and their widgets in your form

class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'align': 'center', 'placeholder': 'Enter a Password'}),
    )

    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'align': 'center', 'placeholder': 'Confirm your password'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter an valid email address'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

