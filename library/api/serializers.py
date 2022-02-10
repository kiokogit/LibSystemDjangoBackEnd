#classes that take a model and turn it into a json object

from rest_framework.serializers import ModelSerializer;
from ..models import Books, BooksInCart, BorrowedBooks, Comments, RequestedBooks, User;

class BookSerializer(ModelSerializer):
    class Meta:
        model=Books;
        fields='__all__';
        
class UserSerializer(ModelSerializer):
    class Meta:
        model=User;
        fields='__all__';
        
class CommentsSerializer(ModelSerializer):
    book = BookSerializer( many=False);
    by = UserSerializer(many=False);
    
    class Meta:
        model=Comments;
        fields='__all__';
        
class CartSerializer(ModelSerializer):
    book = BookSerializer(many=False);
    user = UserSerializer(many=False)
    class Meta:
        model=BooksInCart;
        fields='__all__';
        
class RequestsSerializer(ModelSerializer):
    book = BookSerializer(many=False);
    by = UserSerializer(many=False);
    class Meta:
        model=RequestedBooks;
        fields='__all__';
        
class BorrowedSerializer(ModelSerializer):
    book=RequestsSerializer(many=False);
    class Meta:
        model=BorrowedBooks;
        fields='__all__';
    
    