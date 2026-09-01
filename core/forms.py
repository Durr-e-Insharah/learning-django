from django import forms
from .models import Book
class BookSearchForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label="Select Book")
    