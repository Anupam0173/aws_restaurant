from django.db import models
from Hotelapp.models import Hotel


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    hotel_image = models.ImageField(upload_to="product_image", blank=True)
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="hotel_product", null=True, blank=True)

    def __str__(self):
        return self.name
