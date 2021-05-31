from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from san3a.orders.api.serializers import (
    CartItemSerializer,
    CartItemWriterSerializer,
    CartSerializer,
    CartWriterSerializer,
    OrderSerializer,
    OrderWriterSerializer,
)
from san3a.orders.models import Cart, CartItem, Order


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CartSerializer
        return CartWriterSerializer

    def get_queryset(self):
        return Cart.objects.filter(owner=self.request.user)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CartItemSerializer
        return CartItemWriterSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OrderSerializer
        return OrderWriterSerializer
