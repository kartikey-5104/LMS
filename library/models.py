from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned = models.BooleanField(default=False)

    def is_overdue(self):
        return date.today() > self.due_date and not self.returned
