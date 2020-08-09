from django.contrib import admin
from django.urls import path, include
import books.views

urlpatterns = [
    path('', books.views.index, name='show_book_route'),
    path('view/<book_id>', books.views.view_book_details, name ='view_book_details'),
    path('create', books.views.create_book),
    path('update/<book_id>', books.views.update_book, name='update_book_route'),
    path('delete/<book_id>/', books.views.delete_book, name = 'delete_book_route'),
]