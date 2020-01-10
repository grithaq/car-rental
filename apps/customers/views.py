from django.shortcuts import render,redirect
from .models import Customers
from .forms import CustomersForm
from django.views.generic import  DetailView,FormView,ListView,TemplateView,UpdateView,View



class ListCustomers(ListView):
    template_name = 'customers.html'
    model = Customers
    queryset = Customers.objects.all()

class AddCustomers(FormView):
    template_name = 'add_customers.html'
    form_class = CustomersForm
    success_url = ''


class UpdateCustomers(UpdateView):
    model = Customers
    fields = ['nik_customers']
    template_name_suffix = '_update_form'