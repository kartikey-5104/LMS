from django.contrib import admin
from .models import Book, Loan

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'quantity']

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'borrow_date', 'due_date', 'returned']
