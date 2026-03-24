from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

class BookInstanceInLine(admin.TabularInline):
    model = BookInstance
    readonly_fields = ['uuid']
    extra = 0
    can_delete = False
    fields = ['uuid', 'due_back', 'status']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'display_genre', 'cover']
    inlines = [BookInstanceInLine]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'book', 'due_back', 'status']
    list_filter = ['book', 'due_back', 'status']
    search_fields = ['uuid', 'book__title', 'book__author__last_name']
    list_editable = ['due_back', 'status']

    fieldsets = [
        ('General', {'fields': ('uuid', 'book')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'display_books']
    readonly_fields = ['display_books']

    fieldsets = [
        ('General', {'fields': ('first_name', 'last_name', 'description', 'display_books')}),
    ]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)