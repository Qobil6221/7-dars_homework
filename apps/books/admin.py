from django.contrib import admin

from apps.books.models import Books, BookAuthor, BookReview, BookGenre

admin.site.register([BookReview])


@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ['title']


@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']
