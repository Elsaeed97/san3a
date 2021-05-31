from django.contrib import admin

from san3a.products.models import Category, Color, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "parent_category", "slug"]
    list_per_page = 50
    search_fields = ("name",)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["id", "color"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "product_category",
        "price",
        "available",
        "featured",
        "bestseller",
    ]
    list_per_page = 50
    search_fields = ("name", "price")
    list_editable = ["available", "featured", "bestseller"]
