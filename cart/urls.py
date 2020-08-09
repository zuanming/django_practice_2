from django.urls import path

import cart.views

urlpatterns = [
  path('add/<book_id>', cart.views.add_to_cart, name='add_to_cart'),
  path('view', cart.views.view_cart, name='view_cart'),
  path('remove/<book_id>', cart.views.remove_from_cart, name='remove_from_cart')
]