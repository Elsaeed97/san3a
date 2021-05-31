from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from san3a.orders.api.views import CartItemViewSet, CartViewSet, OrderViewSet
from san3a.products.api.views import CategoryViewSet, ProductViewSet
from san3a.tutorials.api.views import TutorialViewSet
from san3a.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)
router.register("orders", OrderViewSet, basename="Order")
router.register("cart_items", CartItemViewSet)
router.register("cart", CartViewSet, basename="Cart")
router.register("tutorials", TutorialViewSet)


app_name = "api"
urlpatterns = router.urls
