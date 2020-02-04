from django.shortcuts import render,redirect
from .models import Customers
from .forms import *
from django.contrib.auth.models import User
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
        cus = Customers.objects.all()
        return render(request,self.template_name,{
            'cus':cus,
        })

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




class DeleteCustomers(View):
    def get(self,request,id):
        obj = Customers.objects.get(id=id)
        obj.delete()
        return redirect('/customers')

