from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Genre(models.Model):
    title = models.CharField(blank = False, max_length=255)
    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(blank=False, max_length=255)
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(blank=False, max_length=255)
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    authors = models.ManyToManyField('Author')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    cover = CloudinaryField()
    # on_delete=RESTRICT ###if there are children under the same parent to be deteled, cannot be deleted
    # on_delete=NULL ###if there are children under the parent to be deleted, the corresponding class will become null value

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    dob = models.DateField(blank=False)
    books = models.ManyToManyField(Book)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name+" "+self.last_name

