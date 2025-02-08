from django.urls import path, include
from booklist_app.views import book_list, book_detail

urlpatterns = [
    path('list/', book_list, name='book-list'),
    path('<int:pk>/', book_detail, name='book-detail'),
]
