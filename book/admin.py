from django.contrib import admin
from .models import Book, BookAuthor, BookReview


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')


admin.site.register(Book, BookAdmin)
admin.site.register(BookAuthor)
admin.site.register(BookReview)
