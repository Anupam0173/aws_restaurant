from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    opening_hour = models.CharField(max_length=200)
    hotel_image = models.ImageField(upload_to="hotel_image", blank=True)

    def __str__(self):
        return self.name
