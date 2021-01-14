from django.shortcuts import render
from django.views import generic
from .models import Author, Book, Genre, Language, BookInstance


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    num_authors = Author.objects.all().count()

    context = {
        'num_books': num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
    }

    return render(request, 'index.html', context=context)


def book_list(request):
    book_list = Book.objects.all()
    context = {
        "book_list": book_list
    }

    return render(request, "catalog/book_list.html", context=context)

# print(num_books)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author


