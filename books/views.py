from django.shortcuts import render, redirect
from .models import Books

def index(request):
    books = Books.objects.all()
    context = {
        'books' : books,
    }
    return render(request, 'books/index.html', context)

def new(request):
    return render(request, 'books/new.html')

def create(request):
    title = request.POST.get('title')
    author = request.POST.get('author')
    country = request.POST.get('country')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    if request.method == 'POST':
        book = Books(
            title = title,
            author = author,
            country = country,
            genre = genre,
            score = score,
            poster_url = poster_url,
            description = description,
            )
        book.save()
        return redirect('books:detail', book.pk)

def detail(request, pk):
    book = Books.objects.get(pk=pk)
    context = {
        'book' : book,
    }
    return render(request, 'books/detail.html', context)

def edit(request, pk):
    book = Books.objects.get(pk=pk)
    context = {
        'book' : book,
    }
    return render(request, 'books/edit.html', context)

def update(request, pk):
    book = Books.objects.get(pk=pk)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.country = request.POST.get('country')
        book.genre = request.POST.get('genre')
        book.score = request.POST.get('score')
        book.poster_url = request.POST.get('poster_url')
        book.description = request.POST.get('description')

        book.save()
        
        return redirect('books:detail', book.pk)

def delete(request, pk):
    book = Books.objects.get(pk=pk)
    book.delete()
    return redirect('books:index')
