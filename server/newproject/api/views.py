from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import book
from .serializer import BookSerializer

# get is for reading data
@api_view(['GET'])
def get_books(request):
    books = book.objects.all()
    serialized_data = BookSerializer(books, many=True).data
    return Response(serialized_data)

# post is for altering or creating data
@api_view(['POST'])
def create_book(request):
    data =  request.data
    serializer =  BookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def book_details(request, pk):
    try:
        books =  book.objects.get(pk=pk)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        books.delete(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        data = request.data
        serializer = BookSerializer(books, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
