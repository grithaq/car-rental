from django.shortcuts import render, redirect
from .models import Drivers
from django.views import View
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse



class ListDrivers(View):
    template_name = 'driver_list.html'

    def get(self,request):

        driver = Drivers.objects.all()

        return render(request,self.template_name,{
            'driver':driver
        })

class CreateDriver(View):
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



class UpdateDriver(View):
    template_name = ''

    def get(self,request):
        pass
    def post(self,request):
        pass


class DeleteDriver(View):

    def get(self,request,driver_id):

        obj = Drivers.objects.get(id=driver_id)
        obj.delete()

        return redirect('/drivers')


class DriverDetail(View):

    def get(self,request,driver_id):
        pass