from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

User = get_user_model()


class Tutorial(TimeStampedModel):
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"))
    video = models.FileField(_("Video"), upload_to="tutorials/%d", max_length=200)

    def __str__(self):
        return self.title
