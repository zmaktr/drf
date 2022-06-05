from wsgiref.validate import validator

from rest_framework import serializers
from rest_framework.reverse import reverse

from . models import Products
from . import validators
class ProductsSerializer(serializers.ModelSerializer):
    eid_price   = serializers.SerializerMethodField(read_only=True)
    
    # method -1 (for adding url field)
    url         = serializers.SerializerMethodField(read_only=True)
    edit_url    = serializers.SerializerMethodField(read_only=True)
    # method -2 (for adding url field)
    url_link    = serializers.HyperlinkedIdentityField(view_name='product_detail', lookup_field='pk') # HyperlinkedIdentityField works only with ModelSerializer otherwise use to above method
    
    # email       = serializers.EmailField(write_only=True)
    
    # validate title in validators.py
    title = serializers.CharField(validators=[validators.validate_title, validators.validate_title_no_hello, validators.unique_product_title])

    # add another field same as title field 
    title_duplicate = serializers.CharField(source='title', read_only=True)
    class Meta:
        model   = Products
        fields  = [
            'edit_url',
            'url',
            'url_link',
            'pk',
            'title', 
            'title_duplicate',
            'content', 
            'price', 
            'sale_price', 
            'eid_price',
            # 'email',
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
    
    # # over writing default method for email (the default method is create)
    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj



