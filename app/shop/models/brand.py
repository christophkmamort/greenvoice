# 3rd party.
from io import BytesIO
from PIL import Image
import os

# Django.
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils.translation import gettext_lazy as _

# Custom one to one fields.
from .basic_with_relations import BasicApi, BasicBanking, BasicImprint, BasicTax
from .basic import BasicMetaData, BasicPerson, BasicStatus

# Custom functions.
from .functions.brand import brand_branding_upload_path, \
                             brand_person_upload_path


"""
One to one fields.
"""
""" class BrandBranding(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name=_('name'))
    logo = models.ImageField(upload_to=brand_branding_upload_path, blank=True, verbose_name=_('logo'))


class BrandSettings(models.Model):
    backorders = models.BooleanField(default=False, blank=True, verbose_name=_('backorders'))
    free_shipping_from = models.FloatField(blank=True, null=True, verbose_name=_('free shipping from'))
    return_policy_period = models.IntegerField(blank=True, null=True, verbose_name=_('return policy period'))
    return_shipping_costs = models.BooleanField(default=True, blank=True, verbose_name=_('return shipping costs'))
    # TODO: Add stores selection in which brand want's to sell it's products to.


class BrandSettingsSales(models.Model):
    brand_settings = models.ForeignKey(BrandSettings, on_delete=models.CASCADE, related_name='sale', verbose_name=_('brand settings'))
    amount = models.FloatField(blank=True, null=True, verbose_name=_('amount (in %)'))
    from_datetime = models.DateTimeField(verbose_name=_('status from'))
    until_datetime = models.DateTimeField(verbose_name=_('status until'))


class BrandSettingsStatus(BasicStatus):
    brand_settings = models.ForeignKey(BrandSettings, null=True, on_delete=models.CASCADE, related_name='status', verbose_name=_('brand settings')) """


"""
Main fields.
"""
class Brand(models.Model):

    """ class Meta:
        ordering = ['created'] """

    def __str__(self):
        return self.imprint.company_name

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


"""
One to one fields.
"""
class BrandImprint(BasicImprint):
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE, related_name='imprint', verbose_name=_('brand'))


"""
Foreign key fields.
"""
""" class BrandPerson(BasicPerson):
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.CASCADE, related_name='people', verbose_name=_('brand'))
    id_front = models.ImageField(upload_to=brand_person_upload_path, blank=True, verbose_name=_('id front'), unique=True)
    id_back = models.ImageField(upload_to=brand_person_upload_path, blank=True, verbose_name=_('id back'), unique=True) """
