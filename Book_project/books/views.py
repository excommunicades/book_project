from rest_framework import viewsets, status
from rest_framework.response import Response

from books.models import Books
from books.services import BookService
from books.serializers import (

    BooksOut,
    BooksIn,

    )



class BookViewSet(viewsets.ViewSet):

    """Endpoint for all methods related to books."""

    def list(self, request):

        """List all books."""

        queryset = BookService.list_books()
        serializer = BooksOut(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):

        """Returns one book"""

        book = BookService.get_book(pk)

        if not book:

            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BooksOut(book)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):

        """Create a book"""


        serializer = BooksIn(data=request.data)

        if serializer.is_valid():
            return BookService.create_book(serializer)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None):
        """Update book's content"""
        updated_book, errors = BookService.update_book(pk, request.data)
        if updated_book:
            serializer = BooksIn(updated_book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(errors, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, pk=None):

        """Delete a book"""

        if BookService.delete_book(pk):

            return Response({"message": "Book was deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

        return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
