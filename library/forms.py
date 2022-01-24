from dataclasses import fields
from django.forms import ModelForm
from .models import User;

class regForm(ModelForm):
    class Meta:
        fields='__all__';
        model=User;