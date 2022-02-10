from rest_framework.decorators import api_view, authentication_classes;
from rest_framework.authentication import TokenAuthentication;
from rest_framework.authtoken.models import Token;
from rest_framework.response import Response

from django.contrib.auth import authenticate

from .forms import bookForm
from .serializers import BorrowedSerializer, RequestsSerializer, UserSerializer;
from ..models import BorrowedBooks, RequestedBooks, User, Books;

#All views for admin operations - approve request, track books, etc, add books etc
@api_view(['GET', 'POST'])
def loginAdmin(request):
    
    #GET CREDENTIALS
    rawData = request.data
    userEmail = rawData['email'];
    password = rawData['password'];
    
    #check if user exists
    try:
        user = User.objects.get(email=userEmail)
    
    except:
        #not found
        return Response(status=401)  
    #else authenticate    
    authed = authenticate(email=userEmail, password=password)
    
    if authed is None:
        #not authenticated
        return Response(status=401);
    else:
        #if authenticated, check if is admin
        if user.isAdmin:   #returns true if is admin - made by superuser
            #create token
            token = Token.objects.create(user=authed);
            #send as json
            currentUser = {'token':token.key}
            return Response(status=200, data=currentUser)
        else:
            return Response(status=403) #forbidden access(not authorized)

@api_view(['GET'])   
def allPendingRequests(request):
    pending = RequestedBooks.objects.all();
    serialized = RequestsSerializer(pending, many=True);
    return Response(data=serialized.data);

#ALL USERS
@api_view(['GET'])
def allUsers(request):
    users = User.objects.all();
    serialized = UserSerializer(users, many=True);
    return Response(data=serialized.data);

#Unreturned books
@api_view(['GET'])
def borrowedBooks(request):
    books = BorrowedBooks.objects.all();
    serialized = BorrowedSerializer(books, many=True);
    return Response(data=serialized.data);

#Add a book
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def addBook(request):
    rawData = request.data;
    form = bookForm(rawData);
    if form.is_valid():
        form.save();
        return Response(status=200);
    else:
        print(form.errors.as_json());
        return Response(status=500);

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def deleteBook(request, pk):
    book=Books.objects.get(id=pk);
    book.delete();
    return Response(status=200);

#DELETE USER - THAT IS, MAKE INACTIVE.
@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
def deleteUser(request, pk):
    
    return Response(status=200)