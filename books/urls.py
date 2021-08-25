from django.urls import path

from .views import create_book, create_book_form


urlpatterns = [
    path("<int:pk>/", create_book, name="create-book"),
    path('htmx/create-book-form/', create_book_form, name='create-book-form')    
]
