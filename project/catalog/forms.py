from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'ISBN', 'category', 'image', 'total_copies', 'available_copies']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter book title'
            }),

            'author': forms.TextInput(attrs={
                'placeholder': 'Enter author name'
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Enter book description',
                'rows': 4
            }),

            'category': forms.Select(),

            'total_copies': forms.NumberInput(attrs={
                'min': 1
            }),

            'available_copies': forms.NumberInput(attrs={
                'min': 0
            }),
        }