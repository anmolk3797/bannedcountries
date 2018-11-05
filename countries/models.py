from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Country(models.Model):
    code         = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Country Code") )
    label        = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("label") )
    phone        = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("phone") )
    is_active       = models.BooleanField(_("active"), default=False)
    created_at   = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_("Created At"))
    modified_at  = models.DateTimeField(auto_now=True, db_index=True, verbose_name=_("Modified At"))
