from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Book
from .serializers import BookSerializer
from .pagination import BookCursorPagination


class BookListView(ListCreateAPIView):
    """
    GET  -> List books (cursor pagination, filtering, sorting, searching)
    POST -> Create a new book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookCursorPagination

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]

    filterset_fields = ['author', 'published_year', 'title']
    ordering_fields = ['title', 'published_year', 'id']
    search_fields = ['title', 'author']



class BookDetailView(RetrieveUpdateDestroyAPIView):
    """
    GET    -> Retrieve a single book
    PUT    -> Update a book
    DELETE -> Delete a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
