from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from san3a.products.api.serializers import (
    CategorySerialzer,
    ProductSerializer,
    ProductWriterSerializer,
)
from san3a.products.models import Category, Product

from .permissions import IsProductOwnerOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsProductOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProductSerializer
        return ProductWriterSerializer
