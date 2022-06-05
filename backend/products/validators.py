from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . models import Products

# method -1 (validate title)
def validate_title(value):
    qs = Products.objects.filter(title__iexact=value) # iexact is overwrites case sentitive 
    if qs.exists():
        raise serializers.ValidationError(f"{value} already exists. kindly select a unique title")
    return value
# method -2 (validate title)
unique_product_title = UniqueValidator(queryset=Products.objects.all(), lookup='iexact')


def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"{value} word is not allowed")
    return value

