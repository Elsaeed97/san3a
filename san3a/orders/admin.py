from django.contrib import admin

from .models import Cart, CartItem, Order


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "owner", "get_cart_items", "date_ordered", "get_total_cost"]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "quantity", "get_cost"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "city",
        "postal_code",
        "paid",
        "get_total_cost",
    ]
    list_editable = ["paid"]
