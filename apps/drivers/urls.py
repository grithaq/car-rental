from django.contrib import admin
from django.urls import path
from apps.drivers.views import *
urlpatterns = [
    path('', ListDrivers.as_view()),
    path('add_driver', CreateDriver.as_view(),name='add_driver'),
    path('update/<int:driver_id>', UpdateDriver.as_view(),name='update'),
    path('delete/<int:driver_id>', DeleteDriver.as_view(),name='delete'),
    path('detail/<int:driver_id>', DriverDetail.as_view(),name='detail'),
    
]