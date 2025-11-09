from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import views as a module

urlpatterns = [
    # Auth
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Books
    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),

    # Library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Role views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
