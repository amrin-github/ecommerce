from cProfile import label


from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# Login
class Login(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

# Seller

class Seller(models.Model):
    user = models.OneToOneField(Login,on_delete=models.CASCADE,related_name='seller')
    GST_no =models.IntegerField()
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.TextField()

# Customer
class Customer(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.TextField()

# Seller Products
class Product(models.Model):
    user = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    count = models.IntegerField()
    seller_image = models.ImageField(upload_to='product/')

# add to chart
class AddToCart(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='add_to_cart')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='add_product')

# buy
class BuyNow(models.Model):
    user =models.ForeignKey(Customer, on_delete=models.CASCADE, related_name= 'b_cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart')
    status = models.BooleanField(default=0)
    count = models.IntegerField()
    delivery_address = models.TextField()
    delivery_phone_number = models.CharField(max_length=10)


