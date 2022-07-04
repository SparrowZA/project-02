from django import forms
from client.models import Address, Client


class AddressForm(forms.Form):
    address_type = forms.IntegerField()
    street = forms.CharField(
        max_length=1024
    )
    street_number = forms.CharField(
        max_length=10
    )
    unit_number = forms.CharField(
        max_length=10
    )
    building = forms.CharField(
        max_length=250
    )
    area = forms.CharField(
        max_length=250
    )
    city = forms.CharField(
        max_length=250
    )
    province = forms.CharField(
        max_length=250
    )
    country = forms.CharField(
        max_length=250
    )
    code = forms.CharField(
        max_length=6
    )


# ClientInlineFormset = forms.inlineformset_factory(
#     Client, Address, form=AddressForm, extra=2
# )        