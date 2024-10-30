from rest_framework.response import Response
from rest_framework import status

from books.models import Books
from books.serializers import BooksOut, BooksIn


class BookService:

    """Base class for business logic"""

    @staticmethod
    def list_books():
        return Books.objects.all()

    @staticmethod
    def get_book(pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            return None

    @staticmethod
    def create_book(serializer):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def update_book(pk, data):
        try:
            book = Books.objects.get(pk=pk)
            serializer = BooksIn(book, data=data)
            if serializer.is_valid():
                return serializer.save(), None
            return None, serializer.errors
        except Books.DoesNotExist:
            return None, {"error": "Book not found."}

    @staticmethod
    def delete_book(pk):
        try:
            book = Books.objects.get(pk=pk)
            book.delete()
            return True
        except Books.DoesNotExist:
            return False
