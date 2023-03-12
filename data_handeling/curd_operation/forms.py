from django import forms
from .models import CurdModel
from django.contrib.auth.models import User

class CurdForms(forms.ModelForm):
    class Meta:
        model=CurdModel
        fields='__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

