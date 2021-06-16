from rest_framework import serializers
from courses.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'course', 'author', 'price', 'status', 'published')
