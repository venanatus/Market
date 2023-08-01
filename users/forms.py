from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Create any username'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Create any password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


Choises = [
    ('user', 'Покупатель'),
    ('admin', 'Продавец'),
]


class TypeChoise(forms.Form):
    a = forms.ChoiceField(widget=forms.RadioSelect(attrs={'style':'width:10px;height:10px'}), choices=Choises, label='Выберите ')


class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label="Введите ваше имя")
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class': 'select'}), choices=Gender_Choise)


    class Meta:
        model = Profile
        fields = ['full_name', 'gender', 'avatar']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label="Никнейм")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label="Пароль")

    class Meta:
        model = User
        fields = ['username', 'password']



