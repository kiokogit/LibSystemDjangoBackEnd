from django.contrib import admin;
from .models import Books, Comments, BorrowedBooks, RequestedBooks, User;

#register all models here
admin.site.register(User);
admin.site.register(Books);
admin.site.register(Comments);
admin.site.register(BorrowedBooks);
admin.site.register(RequestedBooks);