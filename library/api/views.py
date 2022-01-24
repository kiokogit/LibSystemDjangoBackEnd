from rest_framework.decorators import api_view;
from rest_framework.response import Response
from ..models import Books;
from .serializers import BookSerializer;

@api_view(['GET'])  #SPECIFY METHODS ALLOWED FOR THIS
def getRoutes(request):
    routes=[
        'GET /api/books',
        'GET /api/users'
    ]
    
    return Response(routes);

@api_view(['GET'])
def getBooks(request):
    
    books=Books.objects.all();
    serializer = BookSerializer(books, many=True);
    
    return Response(serializer.data);

def userSignUp(request):
    #receive data from signup form
    if request.method=='POST':
        username=request.POST.get("username");
        
    return Response();
