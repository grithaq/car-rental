from django.shortcuts import render,redirect
from .models import Cars
from django.views import  View
from .forms import CarsForm
from .models import Cars

class KatalogView(View):
    template_name = 'katalog.html'

    def get(self,request):
        cars = Cars.objects.all()

        return render(request, self.template_name,{
            'cars':cars
        })

class TambahKatalogView(View):

    template_name = 'tambah_katalog.html'

    def get(self,request):
        form = CarsForm(request.POST)

        return render(request, self.template_name,{
            'form':form
        })

class SaveKatalogView(View):

    def post(self):
        pass