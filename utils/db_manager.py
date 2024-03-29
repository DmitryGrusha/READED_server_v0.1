from django.http import JsonResponse

from user_module.models import User
from book_module.models import Book


def get_user_from_db(user_id):
    try:
        user = User.objects.get(pk=user_id)
        serialized_user = {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'last_name': user.last_name,
            'country_code': user.country_code,
            'phone_number': user.phone_number,
            'email': user.email
        }
        return True, serialized_user
    except:
        return False, "Serialization error."

def get_book_from_db(book_id):
    try:
        book = Book.objects.get(pk=book_id)
        return True, JsonResponse({ 'id': book.id,
                                    'author': book.author,
                                    'title': book.title,
                                    'storyline': book.storyline,
                                    'chapters_count': book.chapters_total_count,
                                    'genres': book.genres,
                                    'chapters': book.chapters }, status=200)
    except:
        return False, "Serialization error."