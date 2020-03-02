from django.contrib import admin
from .models import Rental,CarsReturn,CarsOut


admin.site.register(Rental)
admin.site.register(CarsReturn)
admin.site.register(CarsOut)