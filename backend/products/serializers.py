from rest_framework import serializers
from rest_framework.reverse import reverse
from . models import Products


class ProductsSerializer(serializers.ModelSerializer):
    eid_price   = serializers.SerializerMethodField(read_only=True)
    url         = serializers.SerializerMethodField(read_only=True)
    edit_url    = serializers.SerializerMethodField(read_only=True)
    url_link      = serializers.HyperlinkedIdentityField(view_name='product_detail', lookup_field='pk') # HyperlinkedIdentityField works only with ModelSerializer otherwise use to above method
    class Meta:
        model   = Products
        fields  = [
            'edit_url',
            'url',
            'url_link',
            'pk',
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
        return obj.holiday_price()

    def get_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        print(request)
        if request is None:
            return None
        return reverse("product_detail", kwargs={"pk": obj.pk},  request=request)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        print(request)
        if request is None:
            return None
        return reverse("product_edit", kwargs={"pk": obj.pk},  request=request)