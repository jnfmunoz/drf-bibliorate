from django.shortcuts import render
from booklist_app.models import Book
from django.http import JsonResponse

# Create your views here.
def book_list(request, *args, **kwargs):
    books = Book.objects.all()
    data = {
        'books': list(books.values())    
        }

    return JsonResponse(data)

def book_detail(request, pk,*args, **kwargs):
    book = Book.objects.get(pk=pk)
    data = {
        'name': book.name,
        'author': book.author,
        'description': book.description,
        'active': book.active,
        }
    
    return JsonResponse(data)