from rest_framework import serializers
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from san3a.products.models import Category, Product


class CategorySerialzer(serializers.ModelSerializer):
    parent_category = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'parent_category']


class ProductSerializer(TaggitSerializer, serializers.ModelSerializer):
    product_category = serializers.StringRelatedField()
    owner = serializers.StringRelatedField(read_only=True)
    created = serializers.SerializerMethodField()
    tags = TagListSerializerField()

    class Meta:
        model = Product
        exclude = ['modified']

    def get_created(self, instance):
        return instance.created.strftime("%B %d %Y")
