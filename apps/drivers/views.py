from django.shortcuts import render, redirect
from .models import Drivers
from django.views import View
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class ListDrivers(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    template_name = 'driver_list.html'

    def get(self,request):

        driver = Drivers.objects.all()

        return render(request,self.template_name,{
            'driver':driver
        })

class CreateDriver(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'

    template_name='add_driver.html'

    def get(self,request):
        form = DriverForm(request.POST)
        return render(request,self.template_name,{
            'form':form
        })
    
    def post(self,request):
        form = DriverForm(request.POST,request.FILES)
        driver = Drivers()
        if request.POST['password']==request.POST['password2']:
            if form.is_valid():
                obj = User.objects.filter(username=request.POST['username'])
                if obj != request.POST['username']:
                    user_name = form.cleaned_data['username']
                    user_password = form.cleaned_data['password']
                    user = User.objects.create_user(username=user_name,password=user_password)
                    user.first_name = form.cleaned_data['first_name']
                    user.last_name = form.cleaned_data['last_name']
                    user.save()
                    driver.user = user
                    driver.nik_driver = form.cleaned_data['nik_driver']
                    driver.driver_phone_number= form.cleaned_data['driver_phone_number']
                    driver.sim_number = form.cleaned_data['sim_number']
                    driver.sim_pict = request.FILES['sim_pict']
                    driver.ktp_pict = request.FILES['ktp_pict']
                    driver.photo_profile = request.FILES['photo_profile']
                    driver.save()

                    return redirect('/drivers')
                else:
                    messages.error(request,'username ini sudah di gunakan')
                    return redirect('/drivers/add_driver')
            return HttpResponse(form.errors)
        messages.error(request,'Password yang anda masukan salah')
        return redirect('/drivers/add_driver')



class EditDriverView(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'

    template_name = 'edit_driver.html'

    def get(self,request,id):
        driver = Drivers.objects.get(id=id)
        data = {
            'id':id,
            'first_name':driver.user.first_name,
            'last_name':driver.user.last_name,
            'nik_driver':driver.nik_driver,
            'driver_phone_number':driver.driver_phone_number,
            'sim_number':driver.sim_number,
            'sim_pict':driver.sim_pict,
            'ktp_pict':driver.ktp_pict,
            'photo_profile':driver.photo_profile,
        }
        form = DriverEditForm(initial=data)

        return render(request,self.template_name,{
            'form':form,
            'id':id
        })
   
class UpdateDriverView(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'


    def post(self,request,id):

        print(request.POST)
        print(request.FILES)
        
        form = DriverEditForm(request.POST,request.FILES)
        print(form.errors)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            print('bisa woiii')
            
            driver = Drivers.objects.get(id=form.cleaned_data['id'])
            user = User.objects.get(id=driver.user.id)
            print(user)

            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            driver.nik_driver = form.cleaned_data['nik_driver']
            driver.driver_phone_number = form.cleaned_data['driver_phone_number']
            driver.nik_driver = form.cleaned_data['nik_driver']
            driver.sim_number = form.cleaned_data['sim_number']
            
            
            
            try:
                driver.sim_pict = request.FILES['sim_pict']
            except Exception:
                pass
            try:
                driver.ktp_pict = request.FILES['ktp_pict']
            except Exception:
                pass
            try:
                driver.photo_profile = request.FILES['photo_profile']
            except Exception:
                pass


            driver.save()

            return redirect('/drivers')
        return HttpResponse(request,form.errors)
        

class DeleteDriver(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'


    def get(self,request,id):

        obj = Drivers.objects.get(id=id)
        obj.delete()

        return redirect('/drivers')


class DriverDetail(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    

    template_name = 'driver_detail.html'

    def get(self,request,id):
        
        driver = Drivers.objects.get(id = id)
        
        return render(request,self.template_name,{
            'driver':driver,
            'id':id
        })
