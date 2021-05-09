from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','description','category','brand','size','gender','product_image')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Product Description'}),
            'category': forms.TextInput(attrs={'class':'form-control','placeholder':'Product Category'}),
            'brand': forms.TextInput(attrs={'class':'form-control','placeholder':'Product Brand'}),
            'size': forms.TextInput(attrs={'class':'form-control','placeholder':'Product Size'}),
            'gender': forms.TextInput(attrs={'class':'form-control','placeholder':'Gender'}),
        }