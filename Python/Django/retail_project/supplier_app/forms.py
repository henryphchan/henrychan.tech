from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['Name', 'ContactPerson', 'ContactEmail', 'PhoneNumber', 'Address', 'ActiveStatus', 'ContractStartDate', 'ContractEndDate']
        widgets = {
            'ActiveStatus': forms.Select(choices=Supplier.ACTIVE_STATUS_CHOICES),
        }
    
    def clean_ContactEmail(self):
        email = self.cleaned_data.get('ContactEmail')
        if email and not forms.EmailField().clean(email):
            raise forms.ValidationError("Please enter a valid email address.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('ContractStartDate')
        end_date = cleaned_data.get('ContractEndDate')

        if start_date and end_date and start_date > end_date:
            self.add_error('ContractStartDate', "Contract start date cannot be greater than contract end date.")
            self.add_error('ContractEndDate', "Contract end date cannot be earlier than contract start date.")

        return cleaned_data