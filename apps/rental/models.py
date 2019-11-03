from django.db import models
from ..customers.models import Customers
from ..cars.models import Cars

class Rental(models.Model):
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    car = models.OneToOneField(Cars,on_delete=models.CASCADE)
    rental_date = models.DateField()
    expire_rental_date = models.DateField()
    payment_pict = models.ImageField(upload_to='image/payment/')
    driver = models.BooleanField(default=False)
    petrol = models.BooleanField(default=False)
    verification = models.BooleanField(default=False)

    def __str__(self):
        return self.rental_date

    class Meta:
        db_table = 'rentals'

