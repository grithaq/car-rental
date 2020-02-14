from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customers(models.Model):
    CHOISES = [
        ('L','Male'),
        ('P','Female')]
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='customers')
    no_telepon = models.CharField(max_length=13)
    nik_customers = models.CharField(max_length=45)
    gender = models.CharField(max_length=2, choices=CHOISES,default='L')
    photo_profile=models.ImageField(upload_to='image/customer/',blank=True,null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'customers'