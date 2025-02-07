from django.shortcuts import render
from booklist_app.models import Book

# Create your views here.
def book_list(request, *args, **kwargs):
    books = Book.objects.all()
    print(books)