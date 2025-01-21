from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    expiry_date = models.DateField()
    # barcode_data = models.TextField(default="None")
    # To store the uploaded barcode image
    # barcode_image = models.ImageField(upload_to='barcodes/')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_name
