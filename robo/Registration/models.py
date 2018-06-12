from django.db import models

# Create your models here.
from django.utils import timezone


class personal(models.Model):

    name = models.CharField(max_length=200)
    Age = models.IntegerField()    
    Address = models.TextField()
    today = models.DateTimeField(
            default=timezone.now)
   

    def publish(self):
        self.today = timezone.now()
        self.save()

    def __str__(self):
        return self.name