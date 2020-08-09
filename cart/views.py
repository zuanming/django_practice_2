from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from books.models import Book
import books

def add_to_cart(request, book_id):
    # attempt to get existing cart from the session using the key "shopping_cart"
    # the second argument will be the default value if 
    # if the key does not exist in the session
    cart = request.session.get('shopping_cart', {})
    
    # we check if the book_is not in the cart. If so, we will add it
    if book_id not in cart:
        book = get_object_or_404(Book, pk=book_id)
        # book is found, let's add it to the cart
        cart[book_id] = {
            'id':book_id,
            'title': book.title,
            'cost': float(book.cost),
            'qty': 1
        } 
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, f"Book {book.title} has been added to your cart!")
        return redirect(reverse('view_cart'))
        # return HttpResponse('book added to cart')
    else:
        cart[book_id]['qty'] +=1
        request.session['shopping_cart'] = cart
        messages.success(request, f"Book has been added to your cart!")
        return redirect(reverse('view_cart'))
        # return HttpResponse('book added to cart')

def view_cart(request):
    cart = request.session['shopping_cart']
    total = 0
    for k, v in cart.items():
        total +=float(v['cost'])
    return render(request, 'cart/view_cart.template.html',{
        'cart':cart,
        "total":total
    })

def remove_from_cart(request, book_id):
    cart = request.session['shopping_cart']
    if book_id in cart:
        del cart[book_id]
        request.session['shopping_cart']=cart
        messages.success(request, f"Book has been removed from  cart")
    
    return redirect(reverse('view_cart'))

def update_quantity(request, book_id):
    cart = request.session['shopping_cart']
    if book_id in cart:
        cart[book_id]['qty'] = request.POST['qty']
        request.session['shopping_cart']=cart
        messages.success(request, f"Quantity for {cart[book_id]['title']} has been updated")
        return redirect(reverse('view_cart'))
    else:
        messages.success(request, f"Error")
        return redirect(reverse('view_cart'))