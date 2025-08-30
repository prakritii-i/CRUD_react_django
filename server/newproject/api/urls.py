from django.urls import path
from .views import get_books, create_book, book_details

urlpatterns = [
    path('books/', get_books, name='get_books'),  # This maps /api/books/ to the get_books view
    path('books/create/',create_book , name='create_book'),
    path('books/<int:pk>/',book_details, name="book_details")
]   
