from rest_framework import serializers

from san3a.orders.models import Cart, CartItem, Order


class CartSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    items = serializers.StringRelatedField(many=True)
    date_ordered = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "owner", "items", "date_ordered"]

    def get_date_ordered(self, instance):
        return instance.date_ordered.strftime("%B %d %Y")


class CartWriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "owner", "items", "date_ordered"]


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "get_cost"]


class CartItemWriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "get_cost"]


class OrderSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()
    cart_items = serializers.StringRelatedField(many=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = [
            "id",
            "owner",
            "first_name",
            "last_name",
            "email",
            "cart_items",
            "city",
            "address",
            "postal_code",
            "paid",
            "get_total_cost",
            "created",
        ]

    def get_created(self, instance):
        return instance.created.strftime("%B %d %Y")


class OrderWriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "owner",
            "first_name",
            "last_name",
            "email",
            "cart_items",
            "city",
            "address",
            "postal_code",
            "paid",
            "get_total_cost",
            "created",
        ]
