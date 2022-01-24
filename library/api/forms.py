from django.forms import Form;
from ..models import User;

class signUpForm(Form):
    class Meta:
        model=User;
        fields='__all__';