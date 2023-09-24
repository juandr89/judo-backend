from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    prefix = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    nit = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField()


class Category(models.Model):
    name = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField()


class Offer(models.Model):
    name = models.CharField(max_length=100)
    discount_percent = models.FloatField()
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    offer = models.ForeignKey(Offer, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=150)
    stock = models.IntegerField()
    price = models.FloatField()
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField()


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='items')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    price = models.FloatField()
    created_at = models.DateTimeField()