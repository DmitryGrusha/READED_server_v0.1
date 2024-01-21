"""READED_server_v01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from user_module.views import register_user, get_user
from book_module.views import load_books, get_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/registerUser/', register_user),
    path('api/getUser/', get_user),

    path('api/createBook/', load_books),
    path('api/getBook/', get_book),
]
