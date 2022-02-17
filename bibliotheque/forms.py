from dataclasses import fields
from typing import OrderedDict
from django import forms
from django.forms import ModelForm
from .models import Book, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import Order






class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']


    




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput({'class':'form-control'})
        }






class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'photo_book',
            'photo_author',
            'document',
            'pages',
            'price',
            'retal_price_day',
            'retal_period',
            'total_rental',
            'status',
            'category',


        ]

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'photo_book': forms.FileInput(attrs={'class':'form-control'}),
            'photo_author': forms.FileInput(attrs={'class':'form-control'}),
            'document': forms.FileInput(attrs={'class':'form-control'}),
            'pages': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'retal_price_day': forms.NumberInput(attrs={'class':'form-control', 'id':'rentalprice'}),
            'retal_period': forms.NumberInput(attrs={'class':'form-control', 'id':'rentaldays'}),
            'total_rental': forms.NumberInput(attrs={'class':'form-control', 'id':'totalrental'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }