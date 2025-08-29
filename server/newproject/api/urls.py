from django.urls import path
from .views import get_books

urlpatterns = [
    path('books/', get_books, name='get_books'),  # This maps /api/books/ to the get_books view
]
