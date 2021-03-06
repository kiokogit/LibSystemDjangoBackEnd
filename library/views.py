from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout;
from django.contrib.auth.decorators import login_required;

from .forms import regForm;
from .models import Books, Comments, User;

# Create your views here.
def homepage(request):
    return render(request, 'library/homepage.html');

def logoutFunc(request):
    logout(request);
    return redirect('home')

def loginPage(request):
    type='login'
    
    if request.method=="POST":
        email=request.POST.get('email');
        password=request.POST.get('password');
        
        try:
            user=User.objects.get(email=email);
        except:
            messages.error(request, 'User does not exist')
    
        user=authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user); #to create the session cookies
            return redirect('dashboard');
        
    context={"type":type}
    
    return render(request, 'library/login_register.html', context);

#registration form
def register(request):
    form=regForm();
    type='register'
    
    if request.method=='POST':
        form=regForm(request.POST);
        if form.is_valid():
            user=form.save()
            login(request, user);
            return redirect('dashboard');
        else:
            messages.error(request, 'User could not be registered');
    
    context={'form':form, 'type':type};
    return render(request, 'library/login_register.html', context);

#login required, else redirect to login
@login_required(login_url='login')
def dashboard(request):
    
    #show all books
    books = Books.objects.all();
    comments=Comments.objects.all();
    context={'books':books, 'comments':comments};
    
    return render(request, 'library/dashboard.html', context);