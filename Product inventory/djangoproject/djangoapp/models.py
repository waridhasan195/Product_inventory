

from django.db import models
from datetime import datetime, date
from django.utils import timezone

# Create your models here.
class Operating_system(models.Model):
    operating_system = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.operating_system


class Computer(models.Model):
    computer_name = models.CharField(max_length=30, blank = True)
    operating_system = models.ForeignKey(Operating_system,max_length = 30, blank = True, null = True, on_delete = models.SET_NULL)
    IP_address = models.CharField(max_length=30)
    MAC_address = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30, blank = True)
    location = models.CharField(max_length=30)
    purchase_date = models.DateField("Purchase Date (mm/dd/yyyy)",auto_now_add = False, auto_now = False, blank=True, null = True)
    timestamp = models.DateField(default=timezone.now, blank = True)
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return self.computer_name
    

