from django import forms
from procat.models import Category,Products

class CategoryForm(forms.Form):
    class Meta:
        model = Category
        
class ProductsForm(forms.Form):
    class Meta:
        model = Products
        fields = ('name','price','description','category')