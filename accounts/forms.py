from django import forms
from accounts.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class customusercreationform(ModelForm):
    class Meta:
        model=User
        fields=['email']
class customuserchangeform(UserChangeForm):
    class Meta:
        model='User'
        fields=['email']
