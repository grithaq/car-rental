from django.db import models
from django.contrib.auth.models import User

class Drivers(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='drivers')
    nik_driver = models.CharField(max_length=45)
    driver_phone_number = models.CharField(max_length=45)
    sim_number = models.CharField(max_length=45)
    sim_pict = models.ImageField(upload_to='image/sim',blank=True,null=True)
    ktp_pict = models.ImageField(upload_to='image/ktp',blank=True,null=True)
    photo_profile = models.ImageField(upload_to='image/profile',blank=True,null=True)


    def __str__(self):
        return self.nik_driver

    class Meta:
        db_table = 'drivers'
