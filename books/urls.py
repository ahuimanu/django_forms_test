from django.urls import path

from .views import create_book


urlpatterns = [
    path('<pk>/', create_book, name='create-book')
]