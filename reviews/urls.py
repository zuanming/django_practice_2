from django.contrib import admin
from django.urls import path, include
import reviews.views


urlpatterns = [
    path('', reviews.views.index, name='show_reviews_route'),
    path('create/<book_id>', reviews.views.create_review, name='create_review_route'),
    path('update/<review_id>/',reviews.views.update_review, name='update_review_route'),
    path('delete/<review_id>/',reviews.views.delete_review, name='delete_review_route'),
    path('create/comment/<review_id>', reviews.views.create_comment, name='create_comment_route'),
]
