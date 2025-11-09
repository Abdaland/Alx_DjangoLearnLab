from django.urls import path
from .views import (
    register_view,
    list_books,
    LibraryDetailView,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book
)

urlpatterns = [
    # Authentication
    path('register/', register_view, name='register'),

    # Books & Library
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Book permissions
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
]
