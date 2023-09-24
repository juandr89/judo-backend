from rest_framework import serializers
from core.models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ['id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        exclude = ['id']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['id']


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        exclude = ['id']