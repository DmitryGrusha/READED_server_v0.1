from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .models import Book
from .serializers import BookSerializer


class CreateBook(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetBookById(APIView):
    def post(self, request):
        book_id = request.data.get('id', None)
        if book_id is None:
            return Response({'message': 'Missing "id" property in the request body.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            book = Book.objects.get(id=book_id)
        except ObjectDoesNotExist:
            return Response({'message': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
