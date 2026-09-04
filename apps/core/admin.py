from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import Book, Review, Bookstore, Award

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 2

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    list_display_links = ('title',)
    list_filter = ('author',)
    inlines = [ReviewInline]

class BookstoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('books',)

class AwardAdmin(admin.ModelAdmin):
    list_display = ('award_name', 'book', 'year_won')

admin.site.register(Book, BookAdmin)
admin.site.register(Bookstore, BookstoreAdmin)
admin.site.register(Award, AwardAdmin)