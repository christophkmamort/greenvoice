from io import BytesIO
from PIL import Image
import os

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils.translation import gettext_lazy as _


def create_upload_path(self, filename):
    return os.path.join('brands', self.name.lower().replace(' ', '-'), 'branding', filename)


class Brand(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'), blank=True)
    logo = models.ImageField(upload_to=create_upload_path, blank=True, verbose_name=_('logo'))
    DRAFT = 1
    PUBLISHED = 2
    PAUSED = 3
    RETIRED = 4
    STATUS_CHOICES = (
        (DRAFT, _('draft')),
        (PUBLISHED, _('published')),
        (PAUSED, _('paused')),
        (RETIRED, _('retired')),
    )
    value = models.FloatField(max_length=200, default=0, verbose_name=_('value'))
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=DRAFT, verbose_name=_('status'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        logo = Image.open(self.logo)
        width = 320
        if logo.size[0] > width:
            hpercent = (width/float(logo.size[0]))
            height = int(logo.size[1]*float(hpercent))
            size = (width, height)
            logo = logo.resize(size, resample=0, box=None)
            thumb_io = BytesIO()
            logo.save(thumb_io, format='JPEG', optimize=True, quality=50)
            inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, None, self.logo.name.split('.')[0] + '.jpg', 'logo/jpeg', thumb_io.tell(), None)
            self.logo = inmemory_uploaded_file
        super(Brand, self).save(*args, **kwargs)
