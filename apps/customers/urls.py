from django.contrib import admin
from django.urls import path
from apps.customers.views import *

urlpatterns = [
    path('', AdminLandingPage.as_view()), #admin landing page
    path('landing_page', MemberLandingPage.as_view()), #customer landing page

    #user
    path('create',CreateUser.as_view(),name='create'), #create customer by admin
    path('update/<int:id>',UpdateUser.as_view(),name='update'),
    path('delete/<int:id>',DeleteUser.as_view(),name='delete'),
    #detail
    path('detail/<int:id>',DetailUser.as_view(),name='detail'),
    path('update_detail/<int:id>',EditDetailUser.as_view(),name='update_detail')
]