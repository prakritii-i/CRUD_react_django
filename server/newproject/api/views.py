from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import book
from .serializer import BookSerializer

@api_view(['GET'])
def get_books(request):
    books = book.objects.all()
    serialized_data = BookSerializer(books, many=True).data
    return Response(serialized_data)
