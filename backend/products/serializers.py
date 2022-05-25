from rest_framework import serializers
from . models import Products


class ProductsSerializer(serializers.ModelSerializer):
    eid_price = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model   = Products
        fields  = [
            'title', 
            'content', 
            'price', 
            'sale_price', 
            'eid_price'
            ]
    # def get_eid_price(self, obj):
    #     try:
    #         return obj.holiday_price()
    #     except: 
    #         return None

    # def get_eid_price(self, obj):
    #     return obj.holiday_price()

    def get_eid_price(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Products):
            return None
        return obj.get_discount()

