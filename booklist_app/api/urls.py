from django.urls import path, include
from .views import EditorialListAV, BookListAV

urlpatterns = [
    path('list/', BookListAV.as_view(), name='book-list'),
    # path('<int:pk>/', book_detail, name='book-detail'),
    path('editorial/list/', EditorialListAV.as_view(), name='editorial-list'),
    
]
