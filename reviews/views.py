from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .forms import ReviewForm, CommentForm, SearchReviewForm
from .models import Review, Comment
from books.models import Book, User
from django.db.models import Q

# Create your views here.


def index(request):
    reviews = Review.objects.all()
    if request.GET:
        query = ~Q(pk__in=[])

        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            query = query &Q(title__icontains=title)
        
        if 'user' in request.GET and request.GET['user']:
            user = request.GET['user']
            query = query &Q(user__username__icontains=user)
        
        if 'book' in request.GET and request.GET['book']:
            books = request.GET['book']
            query = query &Q(books__in=books)
        reviews = reviews.filter(query)
        
    search_review_form = SearchReviewForm(request.GET)
    print(query)
    print(reviews)
    user = User.objects.all()
    books = Book.objects.all()
    return render(request, "reviews/index.template.html", {
        'search_review_form' : search_review_form,
        'reviews': reviews,
        'books':books,

    })


def create_review(request, book_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        # create an instance of review, but don't commit, so that we have a chance to set the user
        review = form.save(commit=False)
        review.user = request.user
        review.book = get_object_or_404(Book, pk=book_id)
        review.save()
        messages.success(
            request, "New review has been added - " + review.title)
        return redirect(reverse('view_reviews_route'))
    else:
        form = ReviewForm()

# def create_review(request, book_id):
#     if request.method == 'POST':
#         review = ReviewForm(request.POST)
#         title = request.POST.get('title')
#         if create_form.is_valid():
#             create_form.save()
#             messages.success(request, f"New review {title} has been created")
#             return redirect(reverse(index))
#         else:
#             return render(request, 'reviews/create_review.template.html', {
#                 'form': create_form
#             })
#     else:
#         create_form = ReviewForm()
#         return render(request, 'reviews/create_review.template.html', {
#             'form': create_form
#         })


def update_review(request, review_id):
    review_being_updated = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review_being_updated)
        title = request.POST.get('title')
        if review_form.is_valid():

            review_form.save()
            messages.success(request, f"Review {title} has been updated")
            return redirect(reverse(index))
        else:
            return render(request, 'reviews/update_review.template.html', {
                'form': create_form
            })
    else:
        review_form = ReviewForm(instance=review_being_updated)
        return render(request, 'reviews/update_review.template.html', {
            'form': review_form
        })


def delete_review(request, review_id):
    review_to_delete = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        review_to_delete.delete()
        messages.success(
            request, f"Review {review_to_delete.title} has been deleted.")
        return redirect(index)

    else:
        return render(request, 'reviews/delete_review.template.html', {
            'review': review_to_delete
        })


def create_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return HttpResponse('Form submitted')
        else:
            return HttpResponse('error with form')

    else:
        form = CommentForm()
        return render(request, 'reviews/create_comment.template.html', {
            'form': form,
            'review': review
        })
