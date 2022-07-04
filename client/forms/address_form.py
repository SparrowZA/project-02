from django import forms
from client.models import Address, Client


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'street',
            'street_number',
            'unit_number',
            'building' ,
            'area' ,
            'city',
            'province',
            'country',
            'code' ,
        ]
        widgets = {
            'address_type': forms.HiddenInput()
        }
