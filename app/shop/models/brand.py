from io import BytesIO
from PIL import Image
import os

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils.translation import gettext_lazy as _

from .api import BasicApi
from .banking import BasicBanking
from .imprint import BasicImprint
from .settings import BrandSettings
from .tax import BasicTax


def create_brand_branding_upload_path(self, filename):
    brand_name = self.name.lower().replace(' ', '-')
    return os.path.join('brands', brand_name, 'branding', filename)


def create_brand_person_upload_path(self, filename):
    brand_name = self.name.lower().replace(' ', '-')
    person_firstname = self.firstname.lower().replace(' ', '-')
    return os.path.join('brands', brand_name, 'people', person_firstname, 'id_card', filename)


class Branding(models.Model):
    brand_name = models.CharField(max_length=200, blank=True, verbose_name=_('brand name'))
    logo = models.ImageField(upload_to=create_brand_branding_upload_path, blank=True, verbose_name=_('logo'))


class Brand(models.Model):
    api = models.OneToOneField(BasicApi, on_delete=models.CASCADE, verbose_name=_('api'))
    branding = models.OneToOneField(Branding, on_delete=models.CASCADE, verbose_name=_('branding'))
    banking = models.OneToOneField(BasicBanking, on_delete=models.CASCADE, verbose_name=_('banking'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    imprint = models.OneToOneField(BasicImprint, on_delete=models.CASCADE, verbose_name=_('imprint'))
    settings = models.OneToOneField(BrandSettings, on_delete=models.CASCADE, verbose_name=_('settings'))
    tax = models.OneToOneField(BasicTax, on_delete=models.CASCADE, verbose_name=_('tax'))
    value = models.FloatField(max_length=200, default=0, verbose_name=_('value'))

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name

    """ def save(self, *args, **kwargs):
        logo = Image.open(self.logo)
        width = 320
        if logo.size[0] > width:
            hpercent = (width / float(logo.size[0]))
            height = int(logo.size[1] * float(hpercent))
            size = (width, height)
            logo = logo.resize(size, resample=0, box=None)
            thumb_io = BytesIO()
            logo.save(thumb_io, format='JPEG', optimize=True, quality=50)
            inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, None, self.logo.name.split(
                '.')[0] + '.jpg', 'logo/jpeg', thumb_io.tell(), None)
            self.logo = inmemory_uploaded_file
        super(Branding, self).save(*args, **kwargs) # Brand """

    # TODO: Automatic path creation for `person id` and `logo`
    # TODO: on save create automatic check if status of live is eligable if not change back to draft.
