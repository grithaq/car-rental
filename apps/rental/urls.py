from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',RentalList.as_view()), #verified rental list
    path('verified_list',VerifiedList.as_view(),name='verified_list'),
    path('verified/<int:id>',Verified.as_view(),name='verified'),
    path('unverified/<int:id>',Unverified.as_view(),name='unverified'),
    path('detail/<int:id>',RentalDetail.as_view(),name='detail'),
    path('edit/<int:id>',Edit.as_view(),name='edit'),
    path('update/<int:id>',Update.as_view(),name='update'),
    path('delete/<int:id>',Delete.as_view(),name='delete'),
    path('create',CreateRent.as_view(),name='create'),


]