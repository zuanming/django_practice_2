from django import forms
from .models import Book, Author, Genre
from django.db.models import Q
from cloudinary.forms import CloudinaryJsFileField

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'desc', 'ISBN', 'cost', 'genre', 'tags','category','authors', 'owner', 'cover')
    cover = CloudinaryJsFileField()

class AuthorForm(forms.Form):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'dob', 'owner')

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    genre = forms.ModelChoiceField(queryset = Genre.objects.all(), required=False)