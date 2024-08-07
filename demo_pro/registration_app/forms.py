from django import forms

from .models import Book


class BookForm(forms.ModelForm):

    class Meta:

        model=Book
        fields='__all__'

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter something about you! '}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your skills '}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your contact details '}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your skills '}),
            'cpassword': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your contact details '}),

        }