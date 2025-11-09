from django.urls import path
from .views import (
    register_view,
    list_books,
    LibraryDetailView,
    admin_view,
    librarian_view,
    member_view
)

urlpatterns = [
    # Registration
    path('register/', register_view, name='register'),

    # List all books
    path('books/', list_books, name='list_books'),

    # Library detail (class-based view)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
