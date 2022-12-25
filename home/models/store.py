from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from uuid import uuid4


class Store(models.Model):
    unique_id = models.UUIDField(_('UUID Code'), blank=True, default=uuid4, editable=False)
    name = models.CharField(_('Store Name'), max_length=250)
    brand_name = models.CharField(_('Brand Name'), max_length=50, null=True)
    company_name = models.CharField(_('Company Name'), max_length=50, null=True)
    web_page_url = models.URLField(_('Web Page URL'), null=True)
    description = models.CharField(_('Description'), max_length=100, null=True)
    is_deleted = models.BooleanField(_('Is Deleted?'), default=False)
    delete_description = models.CharField(_('Description'), max_length=1000, null=True)
    created_at = models.DateTimeField(_('Created Date Time'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated Date Time'), auto_now=True, null=True)

    class Meta:
        ordering = ['name']
        get_latest_by = 'name'
        verbose_name = _('Store')
        verbose_name_plural = _('Stores')

    def __init__(self, *args, **kwargs):
        super(Store, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store', args=[str(self.unique_id)])

    def save(self, *args, **kwargs):
        super(Store, self).save(*args, **kwargs)