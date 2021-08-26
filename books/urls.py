from django.urls import path

from .views import create_book, create_book_form, detail_book


urlpatterns = [
    path("<int:pk>/", create_book, name="create-book"),
    path("htmx/create-book-form/", create_book_form, name="create-book-form"),
    path("htmx/book/<pk>/", detail_book, name="detail-book"),
]
