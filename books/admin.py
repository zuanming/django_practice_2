from django.contrib import admin
from .models import Book, Author, Genre, Category, Tag

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Tag)