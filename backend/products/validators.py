from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . models import Products


def validate_title(value):
    qs = Products.objects.filter(title__iexact=value) # iexact is overwrites case sentitive 
    if qs.exists():
        raise serializers.ValidationError(f"{value} already exists. kindly select a unique title")
    return value

def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"{value} hello word is not allowed")
    return value

unique_product_title = UniqueValidator(queryset=Products.objects.all())
