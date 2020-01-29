from django.urls import path
from apps.customers.views import *

urlpatters = [
    path('landing', MemberLandingPage.as_view()),
]