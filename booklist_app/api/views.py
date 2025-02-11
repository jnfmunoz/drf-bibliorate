from rest_framework.response import Response
from rest_framework.views import APIView
from booklist_app.models import Editorial, Book
from .serializers import EditorialSerializer, BookSerializer

class EditorialListAV(APIView):

    def get(self, request, *args, **kwargs):
        editorials = Editorial.objects.all() 
        serializer = EditorialSerializer(editorials, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = EditorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class BookListAV(APIView):

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class BookDetailAV(APIView):
    
    def get(self, request, *args, **kwargs):
        pass         