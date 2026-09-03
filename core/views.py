from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from .models import Book
from .forms import BookSearchForm, UserRegisterForm

def home(request):
    featured_books = Book.objects.all()[:3]
    return render(request, 'home.html', {'featured_books': featured_books})


def about(request):
    return render(request, 'about.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})


def find_store(request):
    stores = None
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            stores = book.stores.all()
    else:
        form = BookSearchForm()
    return render(request, 'find_store.html', {'form': form, 'stores': stores})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')