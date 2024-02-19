from django.urls import path

from apps.books.views import BookListView, BookDetailView, AuthorView

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name="book-list"),
    path('<slug:slug>', BookDetailView.as_view(), name="book-detail"),
    path('author/<int:pk>', AuthorView.as_view(), name="author"),
]