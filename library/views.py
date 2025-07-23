from django.shortcuts import render, redirect
from .models import Book, Loan
from datetime import timedelta, date
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    books = Book.objects.all()
    return render(request, 'library/dashboard.html', {'books': books})

@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if book.quantity > 0:
        Loan.objects.create(
            user=request.user,
            book=book,
            due_date=date.today() + timedelta(days=14)
        )
        book.quantity -= 1
        book.save()
    return redirect('/')
