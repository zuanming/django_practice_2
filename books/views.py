from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Book, Author
from .forms import BookForm, AuthorForm
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.


def index(request):
    books = Book.objects.all()
    # Pass db data as dictionary to the html
    return render(request, 'books/index.template.html', {
        'books': books
    })


def author(request):
    authors = Author.objects.all()
    return render(request, 'books/authors.template.html', {
        'authors': authors
    })


@login_required
def create_book(request):
    # check if method is post
    if request.method == 'POST':

        # get form input from html
        create_form = BookForm(request.POST)
        title = request.POST.get('title')

        # check if form is valid
        if create_form.is_valid():

            # save form into model
            create_form.save()
            messages.success(request, f"New book {title} has been created")
            # redirect to index function (show books page)
            return redirect(reverse(index))
        else:
            # if not valid, render form again
            return render(request, 'books/create.template.html', {
                'form': create_form
            })
    # if method is get
    else:
        create_form = BookForm()
        return render(request, 'books/create.template.html', {
            'form': create_form
        })

@login_required
def create_author(request):
    if request.method == 'POST':
        create_form = AuthorForm(request.POST)
        name = request.POST.get('first_name')+" "+request.POST.get('last_name')
        if create_form.is_valid():
            create_form.save()
            messages.success(request, f"New author {name} has been created")
            return redirect(reverse(author))
        else:
            return render(request, 'books/create_author.template.html', {
                'form': create_form
            })
    else:
        create_form = AuthorForm()
        return render(request, 'books/create_author.template.html', {
            'form': create_form
        })


def update_book(request, book_id):
    # 1. retrieve the book that we are editing
    book_being_updated = get_object_or_404(Book, pk=book_id)

    # 2. if the update form is submitted
    if request.method == "POST":

        # 3. create the form and fill in the user's data. Also specify that
        # this is to update an existing model (the instance argument)
        book_form = BookForm(request.POST, instance=book_being_updated)
        title = request.POST.get('title')
        if book_form.is_valid():
            book_form.save()
            messages.success(request, f"Book {title} has been updated")
            return redirect(reverse(index))
        else:
            return render(request, 'books/update.template.html', {
                "form": book_form
            })
    else:
        # 4. create a form with the book details filled in
        book_form = BookForm(instance=book_being_updated)
        return render(request, 'books/update.template.html', {
            "form": book_form
        })


def update_author(request, author_id):

    author_being_updated = get_object_or_404(Author, pk=author_id)

    if request.method == "POST":
        author_form = AuthorForm(request.POST, instance=author_being_updated)
        name = request.POST.get('first_name')+" "+request.POST.get('last_name')
        if author_form.is_valid():
            author_form.save()
            messages.success(request, f"Author {name} has been updated")
            return redirect(reverse(author))
        else:
            return render(request, 'books/update_author.template.html', {
                'form': author_form
            })
    else:
        author_form = AuthorForm(instance=author_being_updated)
        return render(request, 'books/update_author.template.html', {
            'form': author_form
        })


def delete_book(request, book_id):
    book_to_delete = get_object_or_404(Book, pk=book_id)
    if request.method=="POST":
        book_to_delete.delete()
        messages.success(request, f"Book {book_to_delete.title} has been deleted")
        return redirect(index)

    else:
        return render(request, 'books/delete_book.template.html', {
            'book':book_to_delete
        })

def delete_author(request, author_id):
    author_to_delete = get_object_or_404(Author, pk=author_id)
    if request.method=="POST":
        author_to_delete.delete()
        messages.success(request, f"Author {author_to_delete.first_name} {author_to_delete.last_name} has been deleted")
        return redirect(author)

    else:
        return render(request, 'books/delete_author.template.html',{
            'author':author_to_delete
        })