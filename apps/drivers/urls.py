from django.contrib import admin
from django.urls import path
from apps.drivers.views import *
urlpatterns = [
    path('', ListDrivers.as_view()),
    path('add_driver', CreateDriver.as_view(),name='add_driver'),
    path('update/<int:id>', UpdateDriverView.as_view(),name='update'),
    path('edit/<int:id>', EditDriverView.as_view(),name='edit'),
    path('delete/<int:id>', DeleteDriver.as_view(),name='delete'),
    path('detail/<int:id>', DriverDetail.as_view(),name='detail'),
    
]