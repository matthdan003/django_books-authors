from django.shortcuts import render, HttpResponse, redirect
from .models import Author, Book

def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'index.html', context)

def add_author(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'add_author.html', context)

def add_book(request):
    Book.objects.create(title=request.POST['title'], description=request.POST['description'])
    return redirect('/')

def get_book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
    }

    assigned_authors = []
    for author in context['book'].authors.all():
        assigned_authors.append(author.id)

    context['authors'] = (Author.objects.exclude(id__in=assigned_authors))
    
    return render(request, 'books.html', context)

def get_author(request, author_id):
    context = {
        'author': Author.objects.get(id=author_id)
    }
    return render(request, 'authors.html', context)

def add_author_book(request, book_id):
    this_book = Book.objects.get(id = book_id)
    this_author = Author.objects.get(id = request.POST['author_id'])

    this_book.authors.add(this_author)
    return redirect('/books/'+str(book_id))