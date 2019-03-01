from rest_framework.serializers import (
    ModelSerializer, SerializerMethodField
) 

from products.models import Product


class ProductSerializer(ModelSerializer):
    category = SerializerMethodField()
    is_pure = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'url', 'id', 'name',
            'category', 'image', 'description',
            'cost', 'is_pure'
        ]

    def get_category(self, obj):
        if obj.category: 
            return obj.category.name

    def get_is_pure(self, obj):
        return obj.created == obj.modified