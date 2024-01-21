from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils import decoder
from book_module.models import create_book

@csrf_exempt
def load_books(request):
    if request.method == 'POST':
        decoder_result, data = decoder.utils_decode(request, [])
        if decoder_result is False: return JsonResponse({'message': 'DECODING ERROR'})
        book_result, book = create_book(author=data.get('author', None),
                                        title=data.get('book_title', None),
                                        storyline=data.get('storyline', None),
                                        chapters_total_count=data.get('chapters_total_count', None),
                                        genres=data.get('genres', None),
                                        chapters=data.get('chapters', None))
        if book_result is False: return JsonResponse({'message': 'CREATE BOOK ERROR'})
        return JsonResponse({'book': {
            'id': book.id,
            'author': book.author,
            'title': book.title,
            'storyline': book.storyline,
            'chapters_total_count': book.chapters_total_count,
            'genres': book.genres,
            'chapters': book.chapters}}, status=200)
    else:
        return JsonResponse({'message': 'ERROR'})


def getBook(request):
    return