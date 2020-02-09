from django.shortcuts import render,redirect
from .models import Customers
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
# from .forms import CustomersForm
from django.views import View
from django.http import HttpResponse
from django.contrib import messages

class MemberLandingPage(View):
    template_name = 'user_landing_page.html'

    def get(self,request):
        cus = Customers.objects.all()

        return render(request,self.template_name,)

class AdminLandingPage(View):
    template_name = 'customers.html'

    def get(self,request):
        user = User.objects.all()
        return render(request,self.template_name,{
            'user':user,
        })

class CreateUser(View):
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


class UpdateUser(View):
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
        # print('Ini adalah reuest dari post',request.POST)
        # print('Ini adalah request File',request.FILES)
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

class DeleteUser(View):
    def get(self,request,id):
        obj = User.objects.get(id=id)
        obj.delete()
        return redirect('/customers')


class CreateCustomers(View):
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


class UpdateCustomers(View):
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


class DetailUser(View):
    template_name = 'detail_user.html'
    def get(self,request,id):
        user = User.objects.get(id=id)
        return render(request,self.template_name,{
            'user':user,
        })

class EditDetailUser(View):
    template_name = 'edit_detail.html'
    def get(self,request,id):
        user = User.objects.get(id=id)
        data={
            'id':id,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'no_telepon':user.customers.no_telepon,
            'nik_customers':user.customers.nik_customers,
            'gender':user.customers.gender,
            'photo_profile':user.customers.photo_profile
        }
        form = EditDetail(initial=data)
        return render(request,self.template_name,{
            'form':form,
            'id':id
        })
    def post(self,request):
        form = EditDetail(request.POST,request.FILES)
        if form.is_valid():
            user = User.objects.get(id=form.cleaned_data['id'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.customers.no_telepon = form.cleaned_data['no_telepon']
            user.customers.nik_customers = form.cleaned_data['nik_customers']
            user.customers.gender = form.cleaned_data['gender']
            user.customers.photo_profile = form.cleaned_data['photo_profile']
            user.save()
            return redirect('/customers')


