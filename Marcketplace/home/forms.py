from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={
        'placeholder': 'Your UserName',
        'class': 'w-full py-4 px-6 rounded-xl'
          }))
    password = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-6 rounded-xl'
          }))
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your UserName',
        'class': 'w-full py-4 px-6 rounded-xl'
          }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Email address',
        'class': 'w-full py-4 px-6 rounded-xl'
          }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-6 rounded-xl'
          }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'w-full py-4 px-6 rounded-xl'
          }))


