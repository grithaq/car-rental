from django.shortcuts import render,redirect
from .models import Customers
from apps.cars.models import Cars
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
# from .forms import CustomersForm
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

class AdminLandingPage(LoginRequiredMixin,View):
    login_url= '/login/'
    redirect_field_name = '/login'
    template_name = 'customers.html'

    def get(self,request):
        cus = Customers.objects.all()
        return render(request,self.template_name,{
            'cus':cus,
        })

class CreateUser(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name = '/login'
    template_name = 'create_user.html'
    def get(self,request):
        form = UserForm(request.POST,request.FILES)
        return render(request,self.template_name,{
            'form':form,
        })
    def post(self,request):
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            if request.POST['password'] == request.POST['password_confirmation']:
                UserName = form.cleaned_data['username']
                pswd = form.cleaned_data['password']
                user = User.objects.create_user(username=UserName,password=pswd)
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                cus = Customers()
                cus.user=user
                cus.photo_profile = request.FILES['photo_profile']
                cus.save()
                return redirect('/customers')
            messages.error(request,'Password tidak sesuai')
            return redirect('/customers/create')
        return HttpResponse(request,form.errors)


class UpdateUser(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name='/login'
    template_name = 'edit_user.html'
    def get(self,request,id):
        user = User.objects.get(id=id)
        photo = user.customers.photo_profile
        # print(user)
        data = {
            'id':id,
            'username':user.username,
            'first_name':user.first_name,
            'password':user.password,

            'last_name':user.last_name,
            'photo_profile':user.customers.photo_profile
        }
        form = UserForm(initial=data)
        # print(form)
        return render(request,self.template_name,{
            'form':form,
            'photo':photo
        })
    def post(self,request,id):
       
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            us = User.objects.get(id=id)
            print(user)
            cus = Customers.objects.get(user=us)
            print(cus)
            us.username = form.cleaned_data['username']
            us.first_name = form.cleaned_data['first_name']
            us.last_name = form.cleaned_data['last_name']
            cus.photo_profile = request.FILES['photo_profile']
            user.save()
            cus.save()
            return redirect('/customers')
        return HttpResponse(request,form.errors)

class DeleteUser(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name = '/login'
    def get(self,request,id):
        obj = Customers.objects.get(id=id)
        obj.delete()
        return redirect('/customers')


class CreateCustomers(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name = '/login'
    template_name = 'add_customers.html'
    def get(self,request):
        form = CreateCustomerForm(request.POST)
        return render(request,self.template_name,{
            'form':form,
        })
    def post(self,request):
        form = CreateCustomerForm(request.POST,request.FILES)
        if form.is_valid():
            cus = Customers()
            if request.POST['password']== request.POST['password_confirmation']:
                print('paswordnya sama lurd :D')
                obj = User.objects.filter(username=request.POST['username'])
                if obj:
                    print('sudah di pake oran lain')
                    messages.error(request,'Username Sudah ada yang pake')
                    return redirect('/customers/create')
                else:
                    user_name = form.cleaned_data['username']
                    password_user = form.cleaned_data['password']
                    user = User.objects.create_user(username=user_name,password=password_user)
                    user.first_name = form.cleaned_data['first_name']
                    user.last_name = form.cleaned_data['last_name']
                    user.save()
                    cus.user = user
                    cus.no_telepon = form.cleaned_data['no_telepon']
                    cus.nik_customers = form.cleaned_data['nik_customers']
                    cus.gender = form.cleaned_data['gender']
                    cus.photo_profile = request.FILES['photo_profile']
                    cus.save()
                    return redirect('/customers')
        return HttpResponse(form.errors)


class UpdateCustomers(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name = '/login'
    template_name='edit_customers.html'
    def get(self,request,id):
        cus = Customers.objects.get(id=id)
        print(type(cus))
        data = {
            'id':id,
            'username':cus.user.username,
            'password':cus.user.password,
            'first_name':cus.user.first_name,
            'last_name':cus.user.last_name,
            'no_telepon':cus.no_telepon,
            'nik_customers':cus.nik_customers,
            'gender':cus.gender,
            'photo_profile':cus.photo_profile
        }
        form = CreateCustomerForm(initial=data)
        return render(request,self.template_name,{
            'form':form
        })
    def post(self,request,id):
        cus = Customers.objects.get(id=id)
        print(cus)
        form = CreateCustomerForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])
            print(user)
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.set_password(form.cleaned_data['password'])
            user.save()
            cus.user = user
            cus.no_telepon = form.cleaned_data['no_telepon']
            cus.nik_customers = form.cleaned_data['nik_customers']
            cus.gender = form.cleaned_data['gender']
            cus.photo_profile = request.FILES['photo_profile']
            cus.save()

            return redirect('/customers')
        return HttpResponse(form.errors)


class DetailUser(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name = '/login'
    template_name = 'detail_user.html'
    def get(self,request,id):
        cus = Customers.objects.get(id=id)
        return render(request,self.template_name,{
            'cus':cus,
        })

class EditDetailUser(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name = '/login'
    template_name = 'edit_detail.html'
    def get(self,request,id):
        cus = Customers.objects.get(id=id)
        data={
            'id':id,
            'first_name':cus.user.first_name,
            'last_name':cus.user.last_name,
            'no_telepon':cus.no_telepon,
            'nik_customers':cus.nik_customers,
            'gender':cus.gender,
            'photo_profile':cus.photo_profile
        }
        form = EditDetail(initial=data)
        return render(request,self.template_name,{
            'form':form,
            'id':id
        })


class UpdateDetailUser(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name='/login'

    def post(self,request,id):
        form = EditDetail(request.POST,request.FILES)
        print('test')
        # print(form)
        if form.is_valid():
            print(form.cleaned_data)
            cus = Customers.objects.get(id=form.cleaned_data['id'])
            user = User.objects.get(id=cus.user.id)
            print(cus)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            cus = Customers.objects.get(user=user)
            cus.no_telepon = form.cleaned_data['no_telepon']
            cus.nik_customers = form.cleaned_data['nik_customers']
            cus.gender = form.cleaned_data['gender']
            print(cus.gender)
            try:
                cus.photo_profile = request.FILES['photo_profile']
            except Exception:
                pass
            
            
            cus.save()
            return redirect('/customers')


#customer view
class MemberLandingPage(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name = '/login'
    template_name = 'customers/user_landing_page.html'

    def get(self,request):
        car = Cars.objects.filter(avaliable=True)
        print('ini adalah usernya',request.user)
        print(car)


        return render(request,self.template_name,{
            'car':car,
        })
class CustomerRent(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ='/login'
    template_name = 'customers/customer_rent.html'
    def get(self,request,car_id):
        print(request.user)
        print(car_id)
        user = User.objects.get(username=request.user)
        car = Cars.objects.get(id=car_id)
        cus = Customers.objects.get(user=user)
        form = CustomerRentForm(request.POST)
        return render(request,self.template_name,{
            'car':car,
            'cus':cus,
            'car_id':car_id,
            'form':form
        })
    
    def post(self,request,car_id):
        form = CustomerRentForm(request.POST)
        print('value of rental date :',request.POST['rental_date'])
        print('class dari rental date',type(request.POST['rental_date']))
        if form.is_valid():
            car = Cars.objects.get(id=car_id)
            print(car)
            user = User.objects.get(username=request.user)
            cus = Customers.objects.get(user=user)
            rent = Rental()
            rent.customer = cus
            rent.car = car
            rent.rental_date = datetime.datetime.strftime(form.cleaned_data['rental_date'],"%Y-%m-%d %H:%M:%S")
            rent.expire_rental_date = datetime.datetime.strftime(form.cleaned_data['expire_rental_date'],"%Y-%m-%d %H:%M:%S")
            rent.driver = form.cleaned_data['driver']
            rent.petrol = form.cleaned_data['petrol']
            rent.save()
            print(rent.id)

            return redirect(f'/customers/billing_detail/{rent.id}')
        return  HttpResponse(form.errors)

class BillingDetail(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name = '/login'
    template_name = 'customers/billing_detail.html'
    def get(self,request,id):
        rent = Rental.objects.get(id=id)
        
        #get count day operation
        d0 = datetime.datetime.strftime(rent.rental_date,"%Y-%m-%d %H:%M:%S")
        d1 = datetime.datetime.strftime(rent.expire_rental_date,"%Y-%m-%d %H:%M:%S")
        mulai = str(d0[-11])+ str(d0[-10])
        print(mulai)
        berakhir = str(d1[-11])+ str(d1[-10])
        print(berakhir)
        awal = int(mulai)
        akhir = int(berakhir)

        count_days= akhir - awal
        print(count_days)

        #get bill operation
        bill = rent.car.price * count_days

        #petrol decription
        if rent.petrol == True:
            petrol_decription = 'yes'
            petrol_amount = 150000
        else:
            petrol_decription = '-'
            petrol_amount = 0
        
        #driver description & payment
        if rent.driver == True:
            driver_description = str(count_days) +' Day'
            driver_payment = 150000
        else:
            driver_description = '-'
            driver_payment = 0
        
        driver_payment = driver_payment*count_days

        total = bill+petrol_amount+driver_payment
        

        return render(request,self.template_name,{
            'rent':rent,
            'id':id,
            'count_days':count_days,
            'bill':bill,
            'petrol_decription':petrol_decription,
            'petrol_amount':petrol_amount,
            'driver_description':driver_description,
            'driver_payment':driver_payment,
            'total':total
        })

class CustomerBriPayment(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name = '/login'
    template_name ='customers/bri_payment.html'
    def get(self,request,id):
        form = CustomerPayment()
        return render(request,self.template_name,{
            'form':form,
            "id":id,
        })
    def post(self,request,id):
        rent = Rental.objects.get(id=id)
        form = CustomerPayment(request.POST,request.FILES)
        if form.is_valid:
            rent.payment_pict = request.FILES['payment_pict']
            car = Cars.objects.get(id=rent.car.id)
            car.avaliable = False
            car.save()
            rent.save()
            return redirect(f'/customers/landing_page')
        return HttpResponse(form)

class CustomerMandiriPayment(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name = '/login'
    template_name ='customers/mandiri_payment.html'
    def get(self,request,id):
        form = CustomerPayment()
        return render(request,self.template_name,{
            'form':form,
            "id":id,
        })
    def post(self,request,id):
        rent = Rental.objects.get(id=id)
        form = CustomerPayment(request.POST,request.FILES)
        if form.is_valid:
            rent.payment_pict = request.FILES['payment_pict']
            car = Cars.objects.get(id=rent.car.id)
            car.avaliable = False
            car.save()
            rent.save()
            return redirect(f'/customers/landing_page')
        return HttpResponse(form)

class CustomerBniPayment(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name = '/login'
    template_name ='customers/bni_payment.html'
    def get(self,request,id):
        form = CustomerPayment()
        return render(request,self.template_name,{
            'form':form,
            "id":id,
        })
    def post(self,request,id):
        rent = Rental.objects.get(id=id)
        form = CustomerPayment(request.POST,request.FILES)
        if form.is_valid:
            rent.payment_pict = request.FILES['payment_pict']
            car = Cars.objects.get(id=rent.car.id)
            car.avaliable = False
            car.save()
            rent.save()
            return redirect(f'/customers/landing_page')
        return HttpResponse(form)


        
        


