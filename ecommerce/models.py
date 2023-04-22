from django.db import models

CATEGORY_CHOICES = (
    ("M", "MALE"),
    ("W", "WOMEN"),
    ("G", "GENERAL")
)



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    image = models.ImageField(upload_to="product_images", default="default.jpg")
    price = models.DecimalField(max_digits=10, decimal_places=2)



    def __str__(self):
        return self.name
