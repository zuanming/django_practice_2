from django.shortcuts import render, reverse, HttpResponse, get_object_or_404

#import settings so that we can access the public stripe key
from django.conf import settings
import stripe

from books.models import Book
from django.contrib.sites.models import Site
 
def checkout(request):
    # tell Stripe what my api_key is
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # retrieve my shopping cart
    cart = request.session.get('shopping_cart', {})


    # SEE EXPLANATION A
    # create our line items
    line_items = []
    all_book_ids = []

    # go through each book in the shopping cart
    for book_id, book in cart.items():
        # retrieve the book by its id from the database
        book_model = get_object_or_404(Book, pk=book_id)

        # create line item
        # you see all the possible properties of a line item at:
        # https://stripe.com/docs/api/invoices/line_item
        item = {
            "name": book_model.title,
            "amount": int(book_model.cost * 100),
            "quantity": book['qty'],
            "currency": "usd",

        }

        line_items.append(item)
        all_book_ids.append(str(book_model.id))

    # get the current website
    current_site = Site.objects.get_current()

    # get the domain name
    domain = current_site.domain


    # SEE EXPLANATION B
    # create a payment session to represent the current transaction
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],  # take credit cards
        line_items=line_items,
        client_reference_id=request.user.id,
        metadata={
            "all_book_ids": ",".join(all_book_ids)
        },
        mode="payment",
        success_url=domain + reverse("checkout_success"),
        cancel_url=domain + reverse("checkout_cancelled")
    )

    return render(request, "checkout/checkout.template.html", {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })


def checkout_success(request):
    return HttpResponse('checkout success')

def checkout_cancelled(request):
    return HttpResponse('checkout failure')