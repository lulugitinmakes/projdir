from django import forms
from .models import Product

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','desc','year','img']