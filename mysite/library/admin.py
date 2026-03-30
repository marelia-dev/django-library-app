from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, BookReview

class BookInstanceInLine(admin.TabularInline):
    model = BookInstance
    readonly_fields = ['uuid']
    extra = 0
    can_delete = False
    fields = ['uuid', 'due_back', 'status']

class BookReviewInLine(admin.TabularInline):
    model = BookReview
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'display_genre', 'cover']
    inlines = [BookReviewInLine, BookInstanceInLine]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'book', 'due_back', 'reader', 'status']
    list_filter = ['book', 'due_back', 'reader', 'status']
    search_fields = ['uuid', 'book__title', 'book__author__last_name']
    list_editable = ['due_back', 'reader', 'status']

    fieldsets = [
        ('General', {'fields': ('uuid', 'book')}),
        ('Availability', {'fields': ('status', 'due_back', 'reader')}),
    ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'display_books']
    readonly_fields = ['display_books']

    fieldsets = [
        ('General', {'fields': ('first_name', 'last_name', 'description', 'display_books')}),
    ]

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'date_created', 'reviewer']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(BookReview, BookReviewAdmin)

