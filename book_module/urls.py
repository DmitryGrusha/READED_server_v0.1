from django.urls import path
from book_module.views import GetBookById, CreateBook

urlpatterns = [
    path('createBook', CreateBook.as_view(), name='create-book'),
    path('getBookById', GetBookById.as_view(), name='get-book-by-id'),
]