from django.shortcuts import render,redirect
from .models import Cars
from django.views import  View
from .forms import CarsForm,CarsEditForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class KatalogView(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    template_name = 'katalog.html'

    def get(self,request):
        
        cars = Cars.objects.all()


        return render(request, self.template_name,{
            'cars':cars
        })

class TambahKatalogView(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'

    template_name = 'tambah_katalog.html'

    def get(self,request):
        form = CarsForm(request.POST)

        return render(request, self.template_name,{
            'form':form
        })
    

class SaveKatalog(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'

    def post(self,request):
        form = CarsForm(request.POST or None,request.FILES or None)
        print(form)
        if form.is_valid():
            car = Cars()
            car.car_name = form.cleaned_data['car_name']
            car.car_brand=form.cleaned_data['car_brand']
            car.cargo_volume = form.cleaned_data['cargo_volume']
            car.seating_capacity = form.cleaned_data['seating_capacity']
            car.price = form.cleaned_data['price']
            car.car_pict = request.FILES['car_pict']
            car.save()

            return redirect('/car')
        return HttpResponse(form.errors)
            

class DeleteKatalog(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'

    def get(self,request,id):

        car = Cars.objects.get(id=id)
        car.delete()

        return redirect('/car')

class UpdateKatalog(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    template_name = 'edit_katalog.html'
    def get(self,request,id):
        print(request.POST)
        # print(request.FILES['car_pict'])
        car = Cars.objects.get(id=id)
        data = {
            'id':id,
            'car_name':car.car_name,
            'car_brand':car.car_brand,
            'seating_capacity':car.seating_capacity,
            'cargo_volume':car.cargo_volume,
            'price':car.price,
            'pict':car.car_pict
        }
        form = CarsEditForm(initial = data)
        print(form)
        return render(request,self.template_name,{
            'form':form
        })


class UbahKatalog(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'

    def post(self,request):
        form = CarsEditForm(request.POST,request.FILES)
        if form.is_valid():
            car = Cars.objects.get(id=form.cleaned_data['id'])
            car.car_name = form.cleaned_data['car_name']
            car.car_brand = form.cleaned_data['car_brand']
            car.seating_capacity =form.cleaned_data['seating_capacity']
            car.cargo_volume = form.cleaned_data['cargo_volume']
            car.price = form.cleaned_data['price']
            try:
                car.car_pict = request.FILES['car_pict']
            except Exception:
                pass
            car.save()

            return redirect('/car')
        return HttpResponse(form.errors)


        