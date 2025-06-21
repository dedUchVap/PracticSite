from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import *
from django import forms
from django.db import models
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'input_my'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'class': 'input_my'}))
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Имя пользователя', 'class': 'input_my'}))

    class Meta:
        model = User
        fields = ['username', 'password1']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Имя пользователя', 'class': 'input_my'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'input_my'}))

    class Meta:
        model = User
        fields = ['username', 'password']