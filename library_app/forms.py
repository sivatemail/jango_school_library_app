from django import forms
from .models import BookStatus,Books
from django.contrib.auth.models import User

class BookStatus_model_form(forms.ModelForm):
    class Meta:
        model = BookStatus
        fields=('book','taken_by')

        widgets={
            'book': forms.Select(attrs={'class':'form-control'}),
            'taken_by': forms.Select(attrs={'class':'form-control'}),
        }
