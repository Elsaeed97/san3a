from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils import Choices


class User(AbstractUser):
    """Default user for San3a Hand Maid."""

    STATUSES = Choices(("client", _("Client")), ("seller", _("Seller")))
    user_type = models.CharField(choices=STATUSES, max_length=15)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
