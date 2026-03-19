from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


class BookInstanceAdmin(admin.TabularInline):
    model = BookInstance
    readonly_fields = ['uuid']
    can_delete = False
    extra = 0
    fields = ['uuid', 'due_back', 'status']

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'display_genre')
    inlines = [BookInstanceAdmin]

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'book', 'status', 'due_back']
    list_filter = ['status', 'due_back']
    search_fields = ['uuid', 'book__title', 'book__author__last_name']
    list_editable = ['due_back', 'status']

    fieldsets = [
        ('General', {'fields': ('uuid', 'book')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    ]
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    readonly_fields = ['display_books']

    fieldsets = [
        ('General', {'fields': ('first_name', 'last_name', 'book')})
        ]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'display_books']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)