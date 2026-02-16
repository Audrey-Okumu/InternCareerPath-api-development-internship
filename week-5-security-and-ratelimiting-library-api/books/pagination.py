from rest_framework.pagination import CursorPagination

class BookCursorPagination(CursorPagination):
    page_size = 5
    ordering = '-id' # newest first 
