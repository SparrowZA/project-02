from django.views.generic import (
    DetailView, 
    ListView, 
    TemplateView,
    )
from django.forms import formset_factory

from multi_form_view import MultiModelFormView

# Forms
from client.forms.client_form import ClientForm
from client.forms.address_form import AddressForm

#Models
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

class ClientForm(MultiModelFormView):
    success_url ="/clients/"
    template_name = "client_create_form.html"

    def forms_valid(self, forms):
        # Make sure to save the client form first.
              
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] =  ClientForm
        address_formset = formset_factory(AddressForm, extra=2, max_num=2)
        formset = address_formset()
        context['formset']= formset

        return context
