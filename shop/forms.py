from django import forms
from .models import Product
class BuyProductForm(forms.Form):
    quantity=forms.IntegerField(help_text="How much quantity do you want to buy.")
    def clean_quantity(self):
        data = self.cleaned_data['quantity']        
        return data        