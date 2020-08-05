from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .forms import ReviewForm
from .models import Review

# Create your views here.


def index(request):
    reviews = Review.objects.all()
    return render(request, "reviews/index.template.html", {
        'reviews': reviews
    })


def create_review(request):
    if request.method == 'POST':
        create_form = ReviewForm(request.POST)
        title = request.POST.get('title')
        if create_form.is_valid():
            create_form.save()
            messages.success(request, f"New review {title} has been created")
            return redirect(reverse(index))
        else:
            return render(request, 'reviews/create_review.template.html', {
                'form': create_form
            })
    else:
        create_form = ReviewForm()
        return render(request, 'reviews/create_review.template.html', {
            'form': create_form
        })


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
        messages.success(request, f"Review {review_to_delete.title} has been deleted.")
        return redirect(index)

    else:
        return render(request, 'reviews/delete_review.template.html', {
            'review': review_to_delete
        })
