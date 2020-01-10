from django.shortcuts import render,redirect
from django.views import  View
from django.contrib.auth import authenticate,login,logout
from .form import LoginForm,RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from apps.customers.models import Customers
from apps.cars.models import Cars
from django.contrib.auth.forms import UserCreationForm

class Base(View):
    template_name ='base/index.html'

    def get(self,request):
        print(dir(request))
        print(request.user)
        return render(request,self.template_name)

class Register(View):
    template_name = 'auth/register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name,{
            'form':form,
            'tittle':'Register'
        })

class RegisterProcess(View):

    def post(self,request):
        print(request.POST)
        print('')
        print(request.FILES)
        print(request.POST['password'])
        print(request.POST['password_confirmation'])
        if request.POST['password']==request.POST['password_confirmation']:
            print('berhasil lurd')
            # return redirect('/car')
            form = RegisterForm(request.POST,request.FILES)
            # print(form)
            cus = Customers()
            # user = User()
            obj = User.objects.filter(username=request.POST['username'])
            print(obj)
            if obj:
                print('bisa bro')
                messages.error(request,'username sudah ada yang pakek bro')
                return redirect('/register')
            elif form.is_valid():  
                print('valid brooooo')
                print('') 
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                print(user_name)
                print(user_password)
                user = User.objects.create_user(username=user_name,password=user_password)
                # user.set_password(user.password)
                user.save()

                cus.user = user
                cus.no_telepon = form.cleaned_data['no_telepon']
                cus.nik_customers = form.cleaned_data['nik_customers']
                cus.gender = form.cleaned_data['gender']
                cus.photo_profile = request.FILES['photo_profile']
                cus.save()
                print(cus)

                return redirect('/car')
            else:
                return redirect('/register')
        else:
            return redirect('/register')
                
        
            



class LoginWeb(View):
    template_name = 'auth/login.html'

    def get(self,request):
        form = LoginForm()

        
        return render(request,self.template_name,{
            'form':form,
            'tittle':'Login',
        })

class LoginProcess(View):

    def post(self,request):
        print(request.POST)
        form = LoginForm(request.POST)
        print(form)

        if form.is_valid():
            print('requestnya valid')
            username_login = form.cleaned_data['username']
            print(username_login)
            password_login = form.cleaned_data['password']
            print(password_login)

            user = authenticate(username=username_login,password=password_login)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('/car')
            messages.error(request,'Username dan Password Tidak di temukan')
            return redirect('/login')
        messages.error(request,'Masukan Username dan Password')
        return redirect('/login')

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('/login')


class AdminKatalog(View):
    template_name = 'admin_car_katalog.html'

    def get(request,self):
        obj = Cars.objects.all()

        return render(request,self.template_name,{
            'obj':obj
        })