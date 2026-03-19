from django.shortcuts import render
from .models import Book, BookInstance, Author
from django.http import HttpResponse


# Create your views here.

# def index(request):
#     return HttpResponse("Labas, pasauli!")

def index(request):
    num_books = Book.objects.count()
    num_instances = Book.objects.count()
    num_authors = Author.objects.count()
    num_instances_available = BookInstance.objects.filter(status='a').count()

    my_context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_authors': num_authors,
        'num_instances_available': num_instances_available,
    }

    return render(request, template_name="index.html", context=my_context)

def about(request):
    return render(request, template_name="about.html")