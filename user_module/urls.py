from django.urls import path
from user_module.views import RegisterUser, GetUserById
#
urlpatterns = [
    path('registerUser', RegisterUser.as_view(), name='register-user'),
    path('getUserById', GetUserById.as_view(), name='get-user-by-id')
]