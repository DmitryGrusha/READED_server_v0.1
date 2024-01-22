from django.urls import path
from .views import CreateBook, GetBookById

urlpatterns = [
    path('createBook', CreateBook.as_view(), name='create-book'),
    path('getBookById', GetBookById.as_view(), name='get-book-by-id'),
]