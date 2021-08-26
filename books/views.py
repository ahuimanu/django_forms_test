from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import BookForm, BookFormSet
from .models import Author, Book

# Create your views here.
def create_book(request, pk):
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author=author)
    # formset = BookFormSet(request.POST or None)
    form = BookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return HttpResponse("success")
        else:
            return render(request, "partials/book_form.html", context={"form": form})
        # if formset.is_valid():
        #     formset.instance = author
        #     formset.save()
        #     return redirect("create-book", pk=author.id)

    context = {
        # "formset": formset,
        "form": form,
        "author": author,
        "books": books,
    }

    return render(request, "create_book.html", context)


def create_book_form(request):
    form = BookForm()
    context = {"form": form}
    return render(request, "partials/book_form.html", context)


def detail_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    context = {"book": book}
    return render(request, "partials/book_detail.html", context)
