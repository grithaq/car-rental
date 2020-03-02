from django.db import models
from ..customers.models import Customers
from ..cars.models import Cars


class Rental(models.Model):
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE,related_name='customer')
    car = models.OneToOneField(Cars,on_delete=models.CASCADE)
    rental_date = models.DateTimeField()
    expire_rental_date = models.DateTimeField()
    payment_pict = models.ImageField(upload_to='image/payment/',blank=True,null=True)
    driver = models.BooleanField(default=False)
    petrol = models.BooleanField(default=False)
    verification = models.BooleanField(default=False)

    def __str__(self):
        return str(self.customer)
    class Meta:
        db_table = 'rentals'
        ordering = ['customer']


class CarsOut(models.Model):
    rent = models.OneToOneField(Rental,on_delete=models.CASCADE,related_name='rent')
    car_out = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rent.customer.user.first_name

    class Meta:
        db_table = 'car_out'
        ordering = ['rent']


class CarsReturn(models.Model):
    rent = models.OneToOneField(Rental,on_delete=models.CASCADE,related_name='rental')
    car_return = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rent.customer.user.first_name

    class Meta:
        db_table = 'car_return'
        ordering = ['rent']

        

