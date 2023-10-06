from rest_framework import serializers
from .models import ProductSlideImage

class ProductSlideImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSlideImage
        fields = "__all__"