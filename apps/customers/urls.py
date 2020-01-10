from django.urls import path
from .views import *

urlpatters = [
    path('',ListCustomers.as_view()),
    path('add',AddCustomers.as_view()),
    path('update',UpdateCustomers.as_view()),
]