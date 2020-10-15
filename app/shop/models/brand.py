# 3rd party.
import os
from io import BytesIO
from PIL import Image

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
Main fields.
"""
class Brand(models.Model):
    pass

    """ class Meta:
        ordering = ['created'] """

    # TODO: Automatic path creation for `person id` and `logo`
    # TODO: on save create automatic check if status of live is eligable if not change back to draft.


"""
One to one fields.
"""
class BrandBranding(models.Model):
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE, related_name='branding', verbose_name=_('brand'))
    brand_name = models.CharField(blank=True, max_length=200, null=True, verbose_name=_('brand name'))
    logo = models.ImageField(blank=True, null=True, upload_to=brand_branding_upload_path, verbose_name=_('logo'), unique=True)

    def save(self, *args, **kwargs):
        # Delete excisting files.
        mydir = str(self.logo.path).replace(self.logo.name, '') + \
                str(brand_branding_upload_path(self, self.logo.name)).replace(self.logo.name, '')
        filelist = [ f for f in os.listdir(mydir) if f.endswith(".jpg") ]
        for f in filelist:
            os.remove(os.path.join(mydir, f))

        # Save new file.
        if self.logo:
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
        super(BrandBranding, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.logo:
            self.logo.delete()
        super(BrandBranding, self).delete(*args, **kwargs)


class BrandImprint(BasicImprint):
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE, related_name='imprint', verbose_name=_('brand'))



""" class BrandSettings(models.Model):
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE, related_name='settings', verbose_name=_('brand'))
    backorders = models.BooleanField(default=False, verbose_name=_('backorders'))
    free_shipping_from = models.FloatField(null=True, blank=True, verbose_name=_('free shipping from'))
    return_policy_period = models.IntegerField(null=True, blank=True, verbose_name=_('return policy period'))
    return_shipping_costs = models.BooleanField(default=True, verbose_name=_('return shipping costs'))
    # TODO: Add stores selection in which brand want's to sell it's products to.

    class Meta:
        verbose_name_plural = _('brand settings')

    def save(self, *args, **kwargs):
        print('brand settings')
        super(BrandSettings, self).save(*args, **kwargs)


class BrandSettingsSales(models.Model):
    brand_settings = models.ForeignKey(BrandSettings, on_delete=models.CASCADE, related_name='sales', verbose_name=_('brand settings'))
    amount = models.FloatField(null=True, blank=True, verbose_name=_('amount (in %)'))
    from_datetime = models.DateTimeField(null=True, blank=True, verbose_name=_('status from'))
    until_datetime = models.DateTimeField(null=True, blank=True, verbose_name=_('status until'))

    class Meta:
        verbose_name_plural = _('brand settings sales')


class BrandSettingsStatus(BasicStatus):
    brand_settings = models.ForeignKey(BrandSettings, on_delete=models.CASCADE, related_name='status', verbose_name=_('brand settings'))

    class Meta:
        verbose_name_plural = _('brand settings status')

    def save(self, *args, **kwargs):
        print('brand settings status')
        super(BrandSettingsStatus, self).save(*args, **kwargs) """


"""
Foreign key fields.
"""
""" class BrandPerson(BasicPerson):
    brand = models.ForeignKey(Brand, blank=True, on_delete=models.CASCADE, related_name='people', verbose_name=_('brand'))
    id_front = models.ImageField(upload_to=brand_person_upload_path, blank=True, verbose_name=_('id front'), unique=True)
    id_back = models.ImageField(upload_to=brand_person_upload_path, blank=True, verbose_name=_('id back'), unique=True) """
