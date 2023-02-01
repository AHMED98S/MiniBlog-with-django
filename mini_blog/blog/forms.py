from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import *

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control form-control-focus'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control form-control-focus'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name':'Last Name', 'email':'Email'}
        widgets = {
                  'username':forms.TextInput(attrs={'class':'form-control form-control-focus'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control form-control-focus'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control form-control-focus'}),
                  'email':forms.EmailInput(attrs={'class':'form-control form-control-focus'}),
                  }



class LoginForm(AuthenticationForm):
   username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 
   'class':'form-control form-control-focus'}))
# autofocus and strip code written in django hidden files
   password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 
   'class':'form-control form-control-focus'}))
# label should be there


class PostForm(forms.ModelForm):
   class Meta:
      model = Post
      fields = ['title', 'desc']
      labels = {'title':'Title', 'desc':'Description'}
      widgets = {
                  'title':forms.TextInput(attrs={'class':'form-control form-control-focus'}),
                  'desc':forms.Textarea(attrs={'class':'form-control form-control-focus'}),
      }
