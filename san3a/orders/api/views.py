from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from san3a.orders.api.serializers import OrderItemSerializer, OrderSerializer
from san3a.orders.models import Order, OrderItem


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = []


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
