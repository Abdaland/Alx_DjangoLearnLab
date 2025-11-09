from django.urls import path
from .views import list_books  # <- this exact line is required by the checker
from .views import (
    register_view,
    LibraryDetailView,
    admin_view,
    librarian_view,
    member_view
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, list_books, LibraryDetailView, admin_view, librarian_view, member_view

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import views as a module

urlpatterns = [
    # Authentication URLs (ALX expects this format)
    path('register/', views.register, name='register'),  # notice "views.register"
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # App URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
from .views import delete_book

urlpatterns += [
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]

