from .models import User;
from django.contrib.auth.forms import UserCreationForm;

class regForm(UserCreationForm):
    class Meta:
        fields=['username', 'email', 'password1', 'password2', 'userEmail', 'firstName', 'lastName'];
        model=User;

        