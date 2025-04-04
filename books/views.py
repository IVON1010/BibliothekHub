from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from .forms import SignupForm
from django.http import HttpResponse
from django.utils.timezone import now, timedelta
from .models import Book, BorrowedBook

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('book-list')
        
    else:
        form = SignupForm()
    return render(request, 'book/signup.html', {
        'form': form
    })

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book-list')
    else:
        form = AuthenticationForm()
    return render(request, 'book/login.html', {
        'form':form
    })

def user_logout(request):
    logout(request)
    return redirect('login')

def book_list(request):
    books = Book.objects.all()
    borrowed_books = BorrowedBook.objects.filter(user=request.user)

    return render(request, 'book/book_list.html', {
        'books': books
    })


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if BorrowedBook.objects.filter(user=request.user, book=book).exists():
        messages.warning(request, "You have already borrowed this book!")
        return redirect('book-list')

    if book.available_copies > 0:
        borrowed_books = BorrowedBook.objects.create(
            user = request.user,
            book = book,
            return_date=now() + timedelta(days=14) 
        )
        book.available_copies -= 1
        book.save()
        messages.success(request, f"You have succcessfully borrowed {book.title}.")
    else:
        messages.error(request, "This book is out of stock!")

    return redirect('book-list')
    
@login_required
def borrowed_books(request):
    books = BorrowedBook.objects.filter(user=request.user)

    return render(request, 'book/borrowed_books.html', {
        'borrowed_books': books
    })

@login_required
def return_book(request, borrow_id):
    borrowed_book = get_object_or_404(BorrowedBook, id=borrow_id, user=request.user)

    borrowed_book.is_returned = True
    borrowed_book.save()

    borrowed_book.book.available_copies += 1
    borrowed_book.book.save()

    return HttpResponse("Book returned successfully!")

