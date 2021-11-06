"""Serializer for Django Rest Framework"""

from rest_framework import serializers
from contacts.models import Contact, Product, Order


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'name', 'email']

    # to reconsider using this - seems like no use:
    # def create(self, validated_data):
    #     return Contact.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.body = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['name', 'ordered_by', 'product']