from django.contrib import admin
from django.urls import path
from apps.customers.views import *

urlpatterns = [
    path('', AdminLandingPage.as_view()), #admin landing page
    #user
    path('create',CreateUser.as_view(),name='create'), #create customer by admin
    path('update/<int:id>',UpdateUser.as_view(),name='update'),
    path('delete/<int:id>',DeleteUser.as_view(),name='delete'),
    #detail
    path('detail/<int:id>',DetailUser.as_view(),name='detail'),
    path('edit_detail/<int:id>',EditDetailUser.as_view(),name='edit_detail'),
    path('update_detail/<int:id>',UpdateDetailUser.as_view(),name='update_detail'),

    #customers url
    path('landing_page/', MemberLandingPage.as_view()), #customer landing page
    path('rent_form/<int:car_id>',CustomerRent.as_view(),name='rent_form'),
    path('billing_detail/<int:id>',BillingDetail.as_view(),name='billing_detail'),
    path('bri_payment/<int:id>',CustomerBriPayment.as_view(),name='bri_payment'),
    path('mandiri_pay/<int:id>',CustomerMandiriPayment.as_view(),name='mandiri_pay'),
    path('bni_pay/<int:id>',CustomerBniPayment.as_view(),name='bni_pay'),
]