from django.contrib import admin
from django.urls import path
from apps.customers.views import *

urlpatterns = [
    path('', AdminLandingPage.as_view()), #admin landing page
    path('landing_page', MemberLandingPage.as_view()), #customer landing page

    path('create',CreateCustomers.as_view(),name='create'), #create customer by admin
    path('update/<int:id>',UpdateCustomers.as_view(),name='update'),
    path('delete/<int:id>',DeleteCustomers.as_view(),name='delete'),

]