from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
]
