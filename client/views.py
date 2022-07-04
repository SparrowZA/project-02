from django.shortcuts import render
from django.views.generic import (
    DetailView, 
    ListView, 
    TemplateView
    )
from django.views.generic.edit import FormView

from client.forms.create_client_form import CreateClientForm
from client.forms.address_form import AddressForm 
from client.models import Address, Client


class HomeView(TemplateView):
    template_name = "home.html"


class ClientList(ListView):
    model = Client
    template_name = "client_list.html"


class ClientDetailView(DetailView):
    model = Client
    template_name = "client_details.html"

    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        context['address'] = Address.objects.all()
        return context

class ClientForm(FormView):
    success_url ="/clients/"

    form_class = CreateClientForm
    
    template_name = "client_create_form.html"

    def form_valid(self, form):
        client = Client(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            id_number=form.cleaned_data['id_number']
        )

        '''addressPostal = Address(
            client=client,
            address_type=0,
            street=form.cleaned_data['street'],
            street_number=form.cleaned_data['street_number'],
            unit_number=form.cleaned_data['unit_number'],
            building=form.cleaned_data['building'],
            area=form.cleaned_data['area'],
            city=form.cleaned_data['city'],
            province=form.cleaned_data['province'],
            country=form.cleaned_data['country'],
            code=form.cleaned_data['code']
        )'''

        client.save()
        addressPostal.save()
        
        return super().form_valid(form)


