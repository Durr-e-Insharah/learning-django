from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookSearchForm(forms.Form):
    book = forms.ModelChoiceField(
        queryset=Book.objects.all(),
        label="Select Book"
    )
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')