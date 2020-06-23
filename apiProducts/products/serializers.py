import uuid
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ('id', 'name', 'value', 'discount_value', 'stock')
    validators = []

  def create(self, validated_data):
    instance = Product()
    instance.id = validated_data.get('id')
    instance.name = validated_data.get('name')
    instance.value = validated_data.get('value')
    instance.discount_value = validated_data.get('discount_value')
    instance.stock = validated_data.get('stock')
    instance.save()
    return instance

  def validate(self, attrs):
    errors = []
    if not 3 < len(attrs["name"]) < 55:
      #raise serializers.ValidationError({"product_id": attrs["id"], "name": "Invalid product name"})
      errors.append("Invalid product name")
    if not 0.0 < float(attrs["value"]) < 99999.9:
      #raise serializers.ValidationError("Invalid value")
      errors.append("Invalid value")
    if attrs["discount_value"] > attrs["value"]:
      #raise serializers.ValidationError("Invalid discount value")
      errors.append("Invalid discount value")
    if attrs["stock"] < 0:
      #raise serializers.ValidationError("Invalid stock value")
      errors.append("Invalid stock value")

    if len(errors) > 0:
      raise serializers.ValidationError({"product_id": str(attrs['id']), "errors": errors})
    return attrs