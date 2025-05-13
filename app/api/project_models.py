from django.db import models
from django.utils import timezone

class Products(models.Model):
    name = models.CharField(max_length=100, default="Unnamed Product")
    description = models.TextField()
    product_image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # No default here

    def __str__(self):
        return self.name

class CartItem(models.Model):
    name = models.CharField(max_length=100, default="Unnamed Item")
    description = models.TextField()
    product_image = models.ImageField(upload_to='Cart_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Only auto_now_add here

    def __str__(self):
        return f"CartItem: {self.name}"

class Payment(models.Model):
    name = models.CharField(max_length=100, default="Anonymous")
    email = models.EmailField()
    address = models.TextField()
    payment_method = models.CharField(max_length=20, choices=[
        ('gcash', 'Gcash'),
        ('maya', 'Maya'),
        ('paypal', 'PayPal')
    ])
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.JSONField()
    receipt_image = models.ImageField(upload_to='avatar/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # No default here

    def __str__(self):
        return f"Payment by {self.name} via {self.payment_method}"
