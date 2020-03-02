from django.shortcuts import render,redirect
from django.views import View
from .models import Rental
from .forms import *
from django.http import HttpResponse
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class RentalList(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    template_name = 'rent_list.html'
    def get(self,request):
        rent = Rental.objects.filter(verification=False)
        return render(request,self.template_name,{
            'rent':rent
        })

class VerifiedList(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    template_name = 'verified_list.html'

    def get(self,request):
        rent = Rental.objects.filter(verification=True)

        return render(request,self.template_name,{
            'rent':rent,
        })
    
class CreateRent(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    template_name = 'create_rent.html'
    def get(self,request):
        form = AdminRentalForm(request.POST)
        return render (request,self.template_name,{
            'form':form,
        })
    def post(self,request):
        form = AdminRentalForm(request.POST,request.FILES)
        print(request.POST)
        print(request.FILES)
        print(form.errors)
        print(form.is_valid)
        if form.is_valid():
            rent = Rental()
            rent.customer = form.cleaned_data['customer']
            rent.car= form.cleaned_data['car']
            rent.rental_date = datetime.datetime.strptime(form.cleaned_data['rental_date'],"%Y-%m-%d %H:%M:%S")
            print(rent.rental_date)
            print(type(rent.rental_date))
            rent.expire_rental_date = datetime.datetime.strptime(form.cleaned_data['expire_rental_date'],"%Y-%m-%d %H:%M:%S")
            print(rent.expire_rental_date)
            print(type(rent.expire_rental_date))
            try:
                rent.payment_pict = request.FILES['payment_pict']
            except Exception:
                pass
            
            rent.driver = form.cleaned_data['driver']
            rent.petrol = form.cleaned_data['petrol']
            rent.save()
            
            return redirect('/rental')
        return HttpResponse(request,form.errors)

class Verified(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    def get(self,request,id):
        rent = Rental.objects.get(id=id)
        rent.verification = True
        rent.save()

        return redirect('/rental')

class Unverified(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    def get(self,request,id):
        rent = Rental.objects.get(id=id)
        rent.verification = False
        rent.save()

        return redirect('/rental/verified_list')

class RentalDetail(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    template_name='rental_detail.html'
    def get(self,request,id):
        rent = Rental.objects.get(id=id)

        return render(request,self.template_name,{
            'rent':rent
        })

class Edit(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    template_name = 'rental_edit.html'
    def get(self,request,id):
        rent=Rental.objects.get(id=id)
        print('type of rental date : ',type(rent.rental_date))
        print('value of rental date : ',rent.rental_date)
        data ={
            'id':id,
            'customer':rent.customer,
            'car':rent.car,
            'rental_date':rent.rental_date,
            'expire_rental_date':rent.expire_rental_date,
            'payment_pict':rent.payment_pict,
            'driver':rent.driver,
            'petrol':rent.petrol,
            'verification':rent.verification,
        }
        form = AdminRentalForm(initial=data)
        return render(request,self.template_name,{
            'form':form,
            'id':id
        })
    
class Update(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    def post(self,request,id):
        form = RentalEditForm(request.POST,request.FILES)
        print(request.POST['id'])
        print(request.FILES)
        print('cek type of rental_date : ',type(request.POST['rental_date']))
        print('cek value of rental_date : ',request.POST['rental_date'])
        print(form.is_valid())
        if form.is_valid():
            rent = Rental.objects.get(id=id)
            rent.customer = form.cleaned_data['customer']
            rent.car = form.cleaned_data['car']
            if type(form.cleaned_data['rental_date'])==datetime.datetime:
                rent.rental_date = form.cleaned_data['rental_date']
            else:
                rent.rental_date = datetime.datetime.strptime(form.cleaned_data['rental_date'],"%Y-%m-%d %H:%M:%S")
            print(type(rent.rental_date))
            if type(form.cleaned_data['expire_rental_date'])==datetime.datetime:
                rent.expire_rental_date=form.cleaned_data['expire_rental_date']
            else:
                rent.expire_rental_date = datetime.datetime.strptime(form.cleaned_data['expire_rental_date'], "%y-%m-%d %H:%M:%D")
            print(type(rent.expire_rental_date))
            try:
                rent.payment_pict= request.FILES['payment_pict']
            except Exception:
                pass
            rent.driver = form.cleaned_data['driver']
            rent.petrol = form.cleaned_data['petrol']
            rent.verification = form.cleaned_data['verification']
            rent.save()
            print(id)
            
            return redirect(f'/rental/detail/{id}')
        return HttpResponse(request,form.errors)



class Delete(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    def get(self,request,id):
        rent = Rental.objects.get(id=id)
        car = Cars.objects.get(id=rent.car.id)
        car.avaliable = True
        car.save()
        rent.delete()
        return redirect('/rental')

class CarOut(LoginRequiredMixin,View):
    pass

class CarReturn(LoginRequiredMixin,View):
    pass
