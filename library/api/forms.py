from django.forms import ModelForm;
from ..models import Books, BooksInCart, Comments, RequestedBooks, User;


class bookForm(ModelForm):
    class Meta:
        model=Books;
        fields='__all__'
        
class userForm(ModelForm):
    class Meta:
        model=User;
        fields='__all__';
        
class commentForm(ModelForm):
    class Meta:
        model=Comments;
        fields='__all__';
        
class inCartForm(ModelForm):
    class Meta:
        model=BooksInCart;
        fields = '__all__';
        
class requestForm(ModelForm):
    class Meta:
        model=RequestedBooks;
        fields='__all__';