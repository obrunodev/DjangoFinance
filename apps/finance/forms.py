from django import forms

from .models import Category
from .models import Spending


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['name']


class SpendingForm(forms.ModelForm):
    
    class Meta:
        model = Spending
        fields = [
            'category',
            'description',
            'expected_cost',
            'real_cost'
        ]
