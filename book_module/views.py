from django.views.decorators.csrf import csrf_exempt
# from utils import decoder, db_manager
# from book_module.models import create_book

# @csrf_exempt
# def load_books(request):
#     if request.method == 'POST':
#         decoder_result, data = decoder.utils_decode(request, [])
#         if decoder_result is False: return JsonResponse({'message': 'DECODING ERROR'}, status=400)
#         book_result, book = create_book(author=data.get('author', None),
#                                         title=data.get('book_title', None),
#                                         storyline=data.get('storyline', None),
#                                         chapters_total_count=data.get('chapters_total_count', None),
#                                         genres=data.get('genres', None),
#                                         chapters=data.get('chapters', None))
#         if book_result is False: return JsonResponse({'message': 'CREATE BOOK ERROR'}, status=400)
#         return JsonResponse({'book': {
#             'id': book.id,
#             'author': book.author,
#             'title': book.title,
#             'storyline': book.storyline,
#             'chapters_total_count': book.chapters_total_count,
#             'genres': book.genres,
#             'chapters': book.chapters}}, status=200)
#     else:
#         return JsonResponse({'message': 'Method not allowed.'}, status=400)
#
#
# @csrf_exempt
# def get_book(request):
#     if request.method == 'POST':
#         decoder_result, data = decoder.utils_decode(request, ['id'])
#         if decoder_result is False: return JsonResponse({'message': 'DECODING ERROR'}, status=400)
#
#         serializable_result, serializable_book = db_manager.get_book_from_db(data.get('id', None))
#         if serializable_result is False: return JsonResponse({'message': "Serialization error."}, status=400)
#
#         return serializable_book
#     else:
#         return JsonResponse({'message': 'Method not allowed.'}, status=400)


from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Book, BookSerializer


class CreateBook(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetBookById(APIView):
    @csrf_exempt
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
