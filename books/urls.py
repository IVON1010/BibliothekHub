from django.urls import path
from .views import signup, user_login, user_logout, borrow_book, borrowed_books, return_book, book_list

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('borrowed/', borrowed_books, name='borrowed_books'),
    path('return/<int:borrow_id>/', return_book, name='return-book'),
    path('books/', book_list, name='book-list'),
]

