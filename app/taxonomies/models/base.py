from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


"""
Fields & Functions for all taxonomies.
"""
class BaseTaxonomy(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name=_('name'))
    slug = models.SlugField(null=True, verbose_name=_('slug'), unique=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        try:
            self.slug = slugify(self.request.data['name'])
        except:
            pass
        return super().save(*args, **kwargs)

    # TODO: Change from category name to category slug on filter logic.