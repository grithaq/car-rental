from django.db import models

# Create your models here.
class Cars(models.Model):
    car_name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    passegers = models.IntegerField()
    baggage = models.IntegerField()
    car_pict = models.ImageField(upload_to='image/cars/')

    def __str__(self):
        return self.car_name

    class Meta:
        db_table = 'cars'