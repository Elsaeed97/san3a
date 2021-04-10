from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from san3a.products.models import Product


class Order(TimeStampedModel):
    first_name = models.CharField(max_length=25, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=25, verbose_name=_("Last Name"))
    email = models.EmailField(verbose_name=_("Email"))
    address = models.CharField(max_length=250, verbose_name=_("Address"))
    postal_code = models.CharField(max_length=20, verbose_name=_("Postal Code"))
    city = models.CharField(max_length=50, verbose_name=_("City"))
    paid = models.BooleanField(default=False, verbose_name=_("Paid"))

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Price")
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Quantity"))

    def __str__(self):
        return str(self.product.name)

    def get_cost(self):
        return self.price * self.quantity
