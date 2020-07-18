from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('books/<int:book_id>', views.get_book),
    path('authors/<int:author_id>', views.get_author),
    path('add_author_book/<int:book_id>', views.add_author_book),
]