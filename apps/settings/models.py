from django.db import models

class Settings(models.Model):
    item = models.CharField(max_length=45)
    value = models.CharField(max_length=45)

    def __str__(self):
        return self.item
    class Meta:
        db_table = 'settings'