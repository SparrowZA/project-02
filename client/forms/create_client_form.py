from django import forms

from client.models import Client, Address
from client.forms.address_form import AddressForm
from client.utils.id_verifier import IdVerifier


class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "id_number"]

    first_name = forms.CharField(label='First Name', max_length=250)
    last_name = forms.CharField(label='Last Name', max_length=250)
    id_number = forms.CharField(label='ID Number', max_length=20)

    def clean_id_number(self):
        id_verifier = IdVerifier()

        id_number = self.cleaned_data['id_number']
        if Client.objects.filter(id_number=id_number).exists():
            raise forms.ValidationError("ID number is not unique")
        
        if not id_verifier.is_valid_id_number(id_number):
            raise forms.ValidationError("Invalid ID number.")
        return id_number

