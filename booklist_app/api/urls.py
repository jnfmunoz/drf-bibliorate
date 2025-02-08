from django.urls import path, include
from .views import BookListAV

urlpatterns = [
    path('list/', BookListAV.as_view(), name='book-list'),
    # path('<int:pk>/', book_detail, name='book-detail'),
]
