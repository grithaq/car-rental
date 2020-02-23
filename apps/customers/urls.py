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
    path('landing_page/<int:customer_id>', MemberLandingPage.as_view()), #customer landing page
    path('rent_form/<int:customer_id>/<int:car_id>',CustomerRent.as_view(),name='rent_form'),
    path('billing_detail/<int:id>',BillingDetail.as_view(),name='billing_detail')
]