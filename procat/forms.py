from django import forms
from django.forms import ModelForm
from procat.models import Category,Products

        
class CategoryForm(ModelForm): 
    class Meta:
        model = Category    
        fields =('name','img')
        
class ProductsForm(ModelForm):      
    class Meta:
        model = Products
        fields = ('name','price','description','category','img')