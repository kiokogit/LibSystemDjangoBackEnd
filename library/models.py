from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name=models.CharField(max_length=200);
    email=models.EmailField(unique=True, null=True);
    bio=models.TextField(null=True, blank=True);
    profilePic=models.ImageField(default='avatar.svg');
    
    USERNAME_FIELD='email';
    REQUIRED_FIELDS=[];
    
    def __str__(self):
        return self.name;
    

class Books(models.Model):
    title=models.CharField(max_length=200);
    author=models.CharField(max_length=200, null=True);
    noOfPages=models.CharField(max_length=200, null=True);
    views=models.CharField(max_length=10, null=True);       
    yearOfPublication=models.DateField(max_length=20, null=True);
    coverImage=models.ImageField( null=True);          #cover thumbnail
    preview=models.TextField(null=True);            #a synopsis of the book, contained in the book info
    category=models.CharField(max_length=200, null=True);          #eg fiction, schoolreader, non-fiction, adventure, novel, short story, class text, periodical, magazine, etc
    discipline=models.CharField(max_length=200, null=True);         #eg philosophy, sociology and social sciences, health sciences, engineering, languages, religion, etc
    subject=models.CharField(max_length=200, null=True);             #eg mathematics, chemistry, theology, nutrition, english Literature, etc
    #tags: [String],                                     #from admin, or made from single words as subject, yearofPublication, 
    RFIDtag=models.CharField(max_length=200, null=True);          #unique identifier
    views=models.CharField(max_length=200, null=True);              #number of times it is clicked by user; helps figure out most popular, or searched
    dateAdded=models.DateTimeField(auto_now_add=True) 
    
    
    def __str__(self):
        return self.title;
    
#comments model
class Comments(models.Model):
    by=models.ForeignKey(User, on_delete=models.CASCADE);
    book=models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    body=models.TextField();
    date=models.DateTimeField(auto_now_add=True);
    #likes=
    
    def __str__(self):
        return self.body;
    
#Requested bookst to be approved - same book can be borrowed by different users
class RequestedBooks(models.Model):
    by=models.ForeignKey(User, on_delete=models.CASCADE);
    book=models.ForeignKey(Books, on_delete=models.CASCADE);
    dateRequested=models.DateTimeField(auto_now=True);
    approved=models.BooleanField(default=False);
    dateApproved=models.DateTimeField();
    
    def __str__(self):
        return self.book.title;
    
#Borrowed Books model - book borrowed must be unique
class BorrowedBooks(models.Model):
    book=models.OneToOneField(RequestedBooks, on_delete=models.CASCADE, unique=True);
    returned=models.BooleanField(default=False);
    dateReturned=models.DateTimeField();
    finesAccumulated=models.CharField(max_length=10);
    
    def __str__(self):
        return self.book.book.title;
