from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from san3a.products.models import Product

User = get_user_model()


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def __str__(self):
        return self.owner.username


class Order(TimeStampedModel):
    cart_items = models.ManyToManyField(CartItem)
    owner = models.ForeignKey(User, verbose_name=_("Owner"), on_delete=models.CASCADE)
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
        return sum(item.get_cost() for item in self.cart_items.all())
