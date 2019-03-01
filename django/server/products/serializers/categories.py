from rest_framework.serializers import ModelSerializer

from products.models import Category
from .products import ProductSerializer


class CategorySerializer(ModelSerializer):
    product_set = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['url', 'id', 'name', 'product_set']
