from rest_framework import serializers


class UserProductInLineSerializer(serializers.Serializer):
    url             = serializers.HyperlinkedIdentityField(view_name='product_detail', lookup_field='pk', read_only=True)
    title           = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username        = serializers.CharField(read_only=True)
    id              = serializers.IntegerField(read_only=True)
    other_products  = serializers.SerializerMethodField(read_only=True)

    # foreign key relationship
    def get_other_products(self, obj):
        print(obj)
        user            = obj
        my_products_qs  = user.products_set.all()[:1]
        return UserProductInLineSerializer(my_products_qs, many=True, context=self.context).data