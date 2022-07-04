from django.urls import path

from client.views import (
    ClientDetailView, 
    ClientList, 
    HomeView,
    ClientForm
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("clients/", ClientList.as_view(), name="client_list"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("client/create/", ClientForm.as_view(), name='client_create_form')
]
