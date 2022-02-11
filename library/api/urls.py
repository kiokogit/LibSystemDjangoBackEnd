from django.urls import path

from . import views, adminViews;

urlpatterns=[
    path('books/', views.getBooks, name='getBooks'),
    path('signup', views.signUpUser, name='signUpUser'),
    
    #user
    path('users/login', views.loginUser, name='loginUser'),
    path('users/logout', views.logOutView, name='logOutUser'),
    path('users/profile/edit', views.editUserProfile, name='editProfile'),
    path('users/submitcomment', views.commentsView, name='submitComment'),
    path('users/comments', views.commentsView, name='getComments'),
    path('users/books/addtocart/<str:pk>', views.inCartView, name='addToCart'),
    path('users/books/removefromcart/<str:pk>', views.inCartView, name='removeFromCart'),
    path('users/books/incart/', views.inCartView, name='getInCart'),
    path('users/books/borrow', views.borrowRequestView, name='borrowBook'),
    path('users/books/cancelorder/<str:pk>', views.borrowRequestView, name='cancelRequest'),
    path('users/borrow/requests', views.borrowRequestView, name='getUserRequests'),
    path('users/borrow/borrowed', views.getBorrowedBooks, name='getUserBorrowed'),
    
    #admin
    path('admin/login', adminViews.loginAdmin, name='loginAdmin'),
    path('admin/users/90', views.getUserDetails, name='user'),
    path('admin/books/edit', views.editBookDetails, name='editBook'),
    path('admin/books/delete/<str:pk>', adminViews.deleteBook, name='deleteBook'),
    path('admin/users/delete/<str:pk>', adminViews.deleteUser, name='deleteUser'),
    path('admin/books/add', adminViews.addBook, name='addBook'),
    path('admin/books/pendingrequests', adminViews.allPendingRequests, name='allRequests'),
    path('admin/books/borrowedbooks', adminViews.borrowedBooks, name='allBorrowed'),
    path('admin/users', adminViews.allUsers, name='allUsers'),
];