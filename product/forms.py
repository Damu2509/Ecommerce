from django import forms
from .models import ItemCategories

class RegisterForm(forms.ModelForm):
    
    class Meta:

        model = ItemCategories

        fields = ['category']

