from rest_framework.decorators import api_view, authentication_classes, permission_classes;
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth import authenticate

from .forms import bookForm, commentForm, inCartForm, requestForm, userForm;
from ..forms import regForm;
from ..models import Books, BooksInCart, BorrowedBooks, Comments, RequestedBooks, User;
from .serializers import BookSerializer, BorrowedSerializer, CartSerializer, CommentsSerializer, RequestsSerializer, UserSerializer;

@api_view(['GET'])
def getBooks(request):
    
    books=Books.objects.all();
    serializer = BookSerializer(books, many=True);
    
    return Response(data=serializer.data);

@api_view(['POST'])
def signUpUser(request):
    #import registration form
    form=regForm();
    
    if request.method=='POST':
        #fill data into form created, and check validity of data: passwords match, email type, etc
        #front end check helps ease the burden of the backend. This check is made in case front end does not verify data validity
        rawData = request.data;        
        email=rawData['userEmail'];
        password1=rawData['userPassword'];
        password2=rawData['confirmPassword'];
        name=rawData['firstName'];
        name2=rawData['lastName'];
        
        #find if user exists
        try:
            User.objects.get(email=email);
            return Response(status=401);
        except:        
            formData={'email':email,'userEmail':email, 'password1':password1, 'password2':password2, 'username':name, 'firstName':name, 'lastName':name2}
        
            form=regForm(formData);
            if form.is_valid():
                form.save(commit=True);
            #send for auto-login(redirecting on client side)
                resData={'email':email, 'password':password1}
                return Response(status=200, data=resData);
            else:
                print(form.error_messages)
                return Response(status=500);
    #all else, 400 - bad request
    else: return
        
@api_view(['POST','OPTIONS'])
def loginUser(request):
    #check out the credentials sent
    rawData = request.data;
    
    #extract email and password
    email=rawData['email'];
    password=rawData['password'];
    try:
        #search if user exists
        User.objects.get(email=email);
    except:
        #User does not exist
        return Response(status=401);
       
       #this authenticate() returns the email
    user=authenticate(email=email, password=password);
    if user is None:
        return Response(status=401)

    else:
        token = Token.objects.create(user=user);
        currentUser = {'token':token.key}
        return Response(status=201, data=currentUser)
  
@api_view(['GET','OPTIONS'])
@authentication_classes([TokenAuthentication])
def logOutView(request):
    
    userEmail = request.user
    user = User.objects.get(email=userEmail)
    token = Token.objects.get(user=user);
    token.delete();
    return Response(status=200);

      
#to access profile details
@api_view(['GET', 'OPTIONS'])
@authentication_classes([TokenAuthentication])
def getUserDetails(request):
    
    userEmail = request.user                #from token authentication class
    
    userDetails = User.objects.get(email=userEmail);
    
    serialized = UserSerializer(userDetails);
    
    return Response(status=200, data=serialized.data);

@api_view(['POST'])
def editBookDetails(request):
    #fetch raw data from request.data
    
    rawData = request.data;
    #extract bookId to find
    bookId = rawData['id'];
    
    book = Books.objects.get(id=bookId)
    
    form=bookForm(instance=book);
    if request.method=='POST':
        form=bookForm(rawData,instance=book);
        if form.is_valid():
            form.save(commit=True); 
            
            #serialize to return to react
            books=Books.objects.all();
            serialized = BookSerializer(books, many=True);
            
            return Response(status=201, data=serialized.data);
        else:
            print(form.errors)
            return Response(status=500);
    
    return Response(status=200);

@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
def editUserProfile(request):
    #data:
    rawData = request.data;
    userEmail=request.user;
    
    user = User.objects.get(email=userEmail);
    
    form = userForm(instance=user);
    if request.method== 'PATCH':
        form = userForm(rawData, instance=user);
        if form.is_valid:
            form.save(commit=True);
            
            #get the user details
            currentUser = User.objects.get(email=userEmail);
            serialized = UserSerializer(currentUser, many=False);
            return Response(status=200, data=serialized.data);
        else:
            return Response(status=404);
    else: return;

#get Comments and post comments
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def commentsView(request):
    
    if request.method=='POST':
        form = commentForm();
        userEmail = request.user        #from authentication - comment is by authenticated user
        commentData = request.data;     #from post form - bookId and comment body
               
        bookId = commentData['book'];
        body=commentData['body'];
    
        #book id is an object, cmpared with a string
        user = User.objects.get(email=userEmail);
        book=Books.objects.get(id=bookId);
    
        formData = {'by':user, 'book':book, 'body':body};
        form = commentForm(formData);
        if form.is_valid():
            comment = form.save(commit=True);
            serialized = CommentsSerializer(comment, many=False);
            return Response(status=200, data=serialized.data);
        
        else:
            print(form.errors.as_json());
            return Response(status=500);       
    
    elif request.method=='GET':
        allComments = Comments.objects.all();
        serialized = CommentsSerializer(allComments, many=True);
        
        return Response(status=200, data=serialized.data);

#cart view
@api_view(['GET','POST','DELETE'])
@authentication_classes([TokenAuthentication])
def inCartView(request, pk=''):
    
    if request.method == 'GET':
         books = BooksInCart.objects.all();
         serialized = CartSerializer(books, many=True);
         
         return Response(status=200, data=serialized.data);
     
    elif request.method == 'POST':
        form = inCartForm();
        userEmail=request.user;
        
        user = User.objects.get(email=userEmail);
        book = Books.objects.get(id=pk);
        formData = {'book':book, 'user':user};
        form = inCartForm(formData);
        if form.is_valid():
            form.save(commit=True);
            
            return Response(status=200);
        else:
            print(form.errors.as_json());
            return Response(status=500);
        
    elif request.method == 'DELETE':
        saved = BooksInCart.objects.get(id=pk);
        saved.delete();
        
        return Response(status=200);
    
    return Response(status=500);

#BORROW A BOOK
@api_view(['GET','POST','DELETE'])
@authentication_classes([TokenAuthentication])
def borrowRequestView(request, pk=''):
    if request.method=='GET':
        #get user borrow requests
        #User:
        userEmail = request.user;
        #Requests
        requests = RequestedBooks.objects.filter(by=userEmail);
        
        serialized = RequestsSerializer(requests, many=True);
        return Response(status=200, data=serialized.data);
    
    elif request.method=='POST':
        #book to borrow
        reqBody = request.data
        bookId = reqBody['bookId'];
        book = Books.objects.get(id=bookId)
        
        #borrower
        userEmail = request.user
        user = User.objects.get(email=userEmail);
        
        #fill form
        formData = {'book':book, 'by':user};
        form = requestForm(formData);
        if form.is_valid():
            form.save(commit=True);
            
            return Response(status=201);
        else:
            print(form.errors.as_json());
            return Response(status=500);
        
    elif request.method=='DELETE':
        #CANCEL REQUEST
        #Request to be cancelled
        request = RequestedBooks.objects.get(id=pk);
        
        #delete
        request.delete();
        
        return Response(status=200);
    return

#BORROWED BOOKS - GET
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def getBorrowedBooks(request):
    
    #for specified user
    user = request.user;
    #borrowed book
    books = BorrowedBooks.objects.filter(book__by=user);
    
    serialized = BorrowedSerializer(books, many=True);
    return Response(data=serialized.data)