from django import forms
from .models import Product

TEXTAREA_CLASS_ATTR = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
NUMBER_CLASS_ATTR = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
SELECT_MULTI_CLASS_ATTR = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name', 'Description', 'Price', 'StockQuantity', 'Suppliers']
        widgets = {
            'Name': forms.TextInput(attrs={
                'class': TEXTAREA_CLASS_ATTR,
                'placeholder': 'Enter product name'
            }),
            'Description': forms.Textarea(attrs={
                'class': TEXTAREA_CLASS_ATTR,
                'rows': 3,
                'placeholder': 'Enter product description'
            }),
            'Price': forms.NumberInput(attrs={
                'class': NUMBER_CLASS_ATTR,
                'placeholder': 'Enter price'
            }),
            'StockQuantity': forms.NumberInput(attrs={
                'class': NUMBER_CLASS_ATTR,
                'placeholder': 'Enter stock quantity'
            }),
            'Suppliers': forms.SelectMultiple(attrs={
                'class': SELECT_MULTI_CLASS_ATTR,
            }),
        }

    def clean_Price(self):
        price = self.cleaned_data.get('Price')
        if price is not None and price < 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price

    def clean_StockQuantity(self):
        stock_quantity = self.cleaned_data.get('StockQuantity')
        if stock_quantity is not None and stock_quantity < 0:
            raise forms.ValidationError("Stock quantity cannot be negative.")
        return stock_quantity
