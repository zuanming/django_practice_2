from django import forms
from .models import Review, Comment
from books.models import Book

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'date', 'books')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class SearchReviewForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    user = forms.CharField(max_length=100, required=False)
    book = forms.ModelChoiceField(queryset=Book.objects.all(), required=False)