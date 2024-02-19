from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from apps.books.models import Books, BookReview
from apps.users.models import User


class BookListView(ListView):
    model = Books
    template_name = "book/book_list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    my_range = range(5)
    model = Books
    slug_url_kwarg = 'slug'
    template_name = "book/book_detail.html"
    context_object_name = "book"


def like_review(request, review_id):
    review = get_object_or_404(BookReview, pk=review_id)
    review.like_count += 1
    review.save()
    return JsonResponse({'like_count': review.like_count})


class ProfileView(ListView):
    model = Books
    template_name = "books/profile.html"
    context_object_name = 'profile'


class AuthorView(DetailView):
    model = User
    template_name = 'book/book_author.html'
    context_object_name = 'author'
    pk_url_kwarg = 'pk'
