from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import contact,Users


class SignupForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
