from django.db import models
from books.models import Book

# Create your models here.
class Review(models.Model):
    title = models.CharField(blank=False, max_length=255)
    content = models.TextField(blank=False)
    date = models.DateField(blank=False)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.title