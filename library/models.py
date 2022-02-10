from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    firstName=models.CharField(max_length=200);
    lastName=models.CharField(max_length=200, null=True, blank=True);
    userPhone=models.CharField(max_length=20, null=True, blank=True);
    email=models.CharField(max_length=200, unique=True, null=True)
    userEmail=models.EmailField( null=True, blank=True);
    dateOfBirth=models.DateField(null=True, blank=True);
    isAdmin=models.BooleanField(default=False);
    gender=models.CharField(max_length=30, null=True, blank=True);
    bio=models.TextField(null=True, blank=True);
    profilePhoto=models.TextField(null=True, blank=True);
    
    USERNAME_FIELD='email';
    REQUIRED_FIELDS=['username'];
    
    def __str__(self):
        return self.email;

class Books(models.Model):
    title=models.CharField(max_length=200);
    author=models.CharField(max_length=200, blank=True, null=True);
    noOfPages=models.CharField(max_length=200, blank=True, null=True);
    views=models.CharField(max_length=10, blank=True, null=True);       
    yearOfPublication=models.DateField(max_length=20, blank=True, null=True);
    coverImage=models.TextField( blank=True, null=True);          #cover thumbnail
    preview=models.TextField(blank=True, null=True);            #a synopsis of the book, contained in the book info
    category=models.CharField(max_length=200, blank=True, null=True);          #eg fiction, schoolreader, non-fiction, adventure, novel, short story, class text, periodical, magazine, etc
    discipline=models.CharField(max_length=200, blank=True, null=True);         #eg philosophy, sociology and social sciences, health sciences, engineering, languages, religion, etc
    subject=models.CharField(max_length=200, blank=True, null=True);             #eg mathematics, chemistry, theology, nutrition, english Literature, etc
    # tags=models.JSONField(blank=True, null=True)                                    #from admin, or made from single words as subject, yearofPublication, 
    RFIDtag=models.CharField(max_length=200, blank=True, null=True);          #unique identifier
    views=models.CharField(max_length=200, blank=True, null=True);              #number of times it is clicked by user; helps figure out most popular, or searched
    dateAdded=models.DateTimeField(auto_now_add=True);
        
    REQUIRED_FIELDS=[];
    
    
    def __str__(self):
        return self.title; 
    
#comments model
class Comments(models.Model):
    by=models.ForeignKey(User, on_delete=models.CASCADE);
    book=models.ForeignKey(Books, on_delete=models.CASCADE, null=True)
    body=models.TextField();
    date=models.DateTimeField(auto_now_add=True);
    
    REQUIRED_FIELDS=[];
    
    def __str__(self):
        return self.body[:50];
    
#Requested bookst to be approved - same book can be borrowed by different users
class RequestedBooks(models.Model):
    by=models.ForeignKey(User, on_delete=models.CASCADE);
    book=models.ForeignKey(Books, on_delete=models.CASCADE, null=True);
    dateRequested=models.DateTimeField(auto_now=True);
    approved=models.BooleanField(default=False);
    dateApproved=models.DateTimeField(null=True, blank=True);
    
    
    def __str__(self):
        return self.book.title;
    
#Borrowed Books model - book borrowed must be unique
class BorrowedBooks(models.Model):
    book=models.OneToOneField(RequestedBooks, on_delete=models.CASCADE, unique=True);
    returned=models.BooleanField(default=False);
    dateReturned=models.DateTimeField(null=True, blank=True);
    finesAccumulated=models.CharField(max_length=10, default=0);
    
    def __str__(self):
        return self.book.book.title;

class BooksInCart(models.Model):
    book=models.ForeignKey(Books, on_delete=models.CASCADE, null=True);
    user = models.ForeignKey(User, on_delete=models.CASCADE);
    
    def __str__(self):
        return self.book.title;
    
