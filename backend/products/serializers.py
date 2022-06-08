from wsgiref.validate import validator

from rest_framework import serializers
from rest_framework.reverse import reverse

from . models import Products
from . import validators
from api.serializers import UserPublicSerializer, UserProductInLineSerializer

class ProductsSerializer(serializers.ModelSerializer):
    
    # related fields can be nested in json
    user            = UserPublicSerializer(read_only=True)
    # related_products= UserProductInLineSerializer(source='user.products_set.all', many=True, read_only=True) 

    eid_price       = serializers.SerializerMethodField(read_only=True)
    
    # method -1 (for adding url field)
    url             = serializers.SerializerMethodField(read_only=True)
    edit_url        = serializers.SerializerMethodField(read_only=True)
    # method -2 (for adding url field)
    url_link        = serializers.HyperlinkedIdentityField(view_name='product_detail', lookup_field='pk') # HyperlinkedIdentityField works only with ModelSerializer otherwise use to above method
    
    # validate title in validators.py
    title           = serializers.CharField(validators=[validators.validate_title, validators.validate_title_no_hello, validators.unique_product_title])

    # add another field same as title field 
    title_duplicate = serializers.CharField(source='title', read_only=True)

    email           = serializers.EmailField(source='user.email', read_only=True)


    class Meta:
        model   = Products
        fields  = [
            'user',
            'email',
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
            # 'related_products',
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
        # print(request)
        if request is None:
            return None
        return reverse("product_detail", kwargs={"pk": obj.pk},  request=request)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        # print(request)
        if request is None:
            return None
        return reverse("product_edit", kwargs={"pk": obj.pk},  request=request)
    
    # # over writing default method for email (the default method is create)
    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj




