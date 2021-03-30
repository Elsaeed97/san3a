from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from model_utils.models import TimeStampedModel

from san3a.products.utils import generate_random_string


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name=_("Category Name"))
    slug = models.SlugField(verbose_name=_("Category Slug"))
    parent_category = models.ForeignKey("self", limit_choices_to={'parent_category__isnull': True},
                                        verbose_name=_("Parent Category"), on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(verbose_name=_("Category Description"))
    image = models.ImageField(verbose_name=_("Category Image"), upload_to='category/')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug) + generate_random_string()
        super(Category, self).save(*args, **kwargs)


class Product(TimeStampedModel):
    owner = models.ForeignKey(get_user_model(), related_name='product',
                              on_delete=models.CASCADE, verbose_name=_("Product Owner"))
    name = models.CharField(max_length=30, verbose_name=_("Product Name"))
    image = models.ImageField(upload_to='product/', verbose_name=_("Image"))
    slug = models.SlugField()
    product_category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name=_("Product Category"))
    description = models.TextField(verbose_name=_("Product Description"))
    price = models.DecimalField(decimal_places=2, max_digits=6, verbose_name=_("Product Price"))
    tags = TaggableManager()
    available = models.BooleanField(default=True, verbose_name=_("Available"))
    featured = models.BooleanField(default=False, verbose_name=_("Featured"))
    bestseller = models.BooleanField(default=False, verbose_name=_("BestSeller"))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug) + generate_random_string()
        super(Product, self).save(*args, **kwargs)
