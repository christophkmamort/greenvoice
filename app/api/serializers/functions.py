VALID_IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
]

def valid_url_extension(url, extension_list=VALID_IMAGE_EXTENSIONS):
    return any([url.endswith(e) for e in extension_list])


import httplib

def image_exists(domain, path):
    try:
        conn = httplib.HTTPConnection(domain)
        conn.request('HEAD', path)
        response = conn.getresponse()
        conn.close()
    except:
        return False
    return response.status == 200


""" def image_exists(domain, path, check_size=False, size_limit=1024):
    try:
        conn = httplib.HTTPConnection(domain)
        conn.request('HEAD', path)
        response = conn.getresponse()
        headers = response.getheaders()
        conn.close()
    except:
        return False

    try:
        length = int([x[1] for x in headers if x[0] == 'content-length'][0])
    except:
        length = 0
    if length > MAX_SIZE:
        return False

    return response.status == 200 """


import requests
import StringIO

def retrieve_image(url):
    response = requests.get(url)
    return StringIO.StringIO(response.content)
    

""" import urllib2
import StringIO

def retrieve_image(url):
    return StringIO.StringIO(urllib2.urlopen(url).read()) """


""" import magic

VALID_IMAGE_MIMETYPES = [
    "image"
]

def get_mimetype(fobject):
    mime = magic.Magic(mime=True)
    mimetype = mime.from_buffer(fobject.read(1024))
    fobject.seek(0)
    return mimetype

def valid_image_mimetype(fobject):
    mimetype = get_mimetype(fobject)
    if mimetype:
        return mimetype.startswith('image')
    else:
        return False """


""" MAX_SIZE = 4*1024*1024

def valid_image_size(image, max_size=MAX_SIZE):
    width, height = image.size
    if (width * height) > max_size:
        return (False, "Image is too large")
    return (True, image) """


""" import os
import StringIO
from urlparse import urlparse
from django.core.files.base import ContentFile

def split_url(url):
    parse_object = urlparse(url)
    return parse_object.netloc, parse_object.path

def get_url_tail(url):
    return url.split('/')[-1]

def get_extension(filename):
    return os.path.splitext(filename)[1]

def pil_to_django(image, format="JPEG"):
    fobject = StringIO.StringIO()
    image.save(fobject, format=format)
    return ContentFile(fobject.getvalue()) """


""" from django.db import models
import os, datetime
from django.utils.text import slugify

UPLOAD_PATH = "image_uploader/"

class UploadedImage(models.Model):
    def generate_upload_path(self, filename):
        filename, ext = os.path.splitext(filename.lower())
        filename = "%s.%s%s" % (slugify(filename),datetime.datetime.now().strftime("%Y-%m-%d.%H-%M-%S"), ext)
        return '%s/%s' % (UPLOAD_PATH, filename)

    image = models.ImageField(blank=True, null=True, upload_to=generate_upload_path) """


""" from .utils import *

from django.utils.translation import ugettext as _
from django import forms


class UploadURLForm(forms.Form):
    url = forms.URLField(required=True,
        error_messages={
            "required": "Please enter a valid URL to an image (.jpg .jpeg .png)"
        },
    )

    def clean_url(self):
        url = self.cleaned_data['url'].lower()
        domain, path = split_url(url)
        if not valid_url_extension(url) or not valid_url_mimetype(url):
            raise forms.ValidationError(_("Not a valid Image. The URL must have an image extensions (.jpg/.jpeg/.png)"))
        return url """


""" from PIL import Image
from django.views.generic.edit import FormView
from django.views.generic import DetailView
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from .forms import UploadURLForm
from .utils import *
from .models import UploadedImage


class UploadURLView(FormView):
    form_class = UploadURLForm
    template_name = "image_uploader/upload.html"

    def get_success_url(self):
        return reverse("upload-detail", args=[self.uploaded_image.pk, ])

    def form_valid(self, form):
        def _invalidate(msg):
            form.errors['url'] = [msg, ]
            return super(UploadURLView, self).form_invalid(form)

        url = form.data['url']
        domain, path = split_url(url)
        filename = get_url_tail(path)

        if not image_exists(domain, path):
            return _invalidate(_("Couldn't retreive image. (There was an error reaching the server)"))

        fobject = retrieve_image(url)
        if not valid_image_mimetype(fobject):
            return _invalidate(_("Downloaded file was not a valid image"))

        pil_image = Image.open(fobject)
        if not valid_image_size(pil_image)[0]:
            return _invalidate(_("Image is too large (> 4mb)"))

        django_file = pil_to_django(pil_image)
        self.uploaded_image = UploadedImage()
        self.uploaded_image.image.save(filename, django_file)
        self.uploaded_image.save()

        return super(UploadURLView, self).form_valid(form)

class UploadDetailView(DetailView):
    model = UploadedImage
    context_object_name = "image"
    template_name = "image_uploader/detail.html" """
