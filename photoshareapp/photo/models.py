from django.db import models
from django.contrib.auth.models import User
from time import time
from django.core.urlresolvers import reverse

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)

def get_upload_file_name_thumb(instance, filename):
    return "uploaded_files/thumb_%s_%s" % (str(time()).replace('.','_'),filename)

class PhotoCategory(models.Model):
    category=models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return self.category

    def __str__ (self):
        return self.category

class PhotoManager(models.Manager):
    def public_photo_count(self, user):
        cat=PhotoCategory.objects.filter(category='Public')
        return self.filter(uploaded=user,category=cat).count()
    def community_photo_count(self, user):
        cat=PhotoCategory.objects.filter(category='Community')
        return self.filter(uploaded=user,category=cat).count()

class Photo(models.Model):
    title=models.CharField("Photo Title:",max_length=100)
    description=models.TextField("Description: ",max_length=250,blank=True)
    uploaded=models.ForeignKey(User)
    category=models.ForeignKey(PhotoCategory)
    image = models.ImageField(upload_to=get_upload_file_name)
    thumbnail = models.ImageField(null=True,blank=True)

    objects=PhotoManager()

    def __unicode__(self):
        return self.title

    def __str__ (self):
        return self.title

    def get_absolute_url(self):
        return reverse("photo_detail",kwargs={"pk":str(self.id)})

    def create_thumbnail(self):

         if not self.image:
             return

         from PIL import Image
         from io import StringIO, BytesIO

         from django.core.files.uploadedfile import SimpleUploadedFile
         import os

         THUMBNAIL_SIZE = (200,200)

         DJANGO_TYPE = self.image.file.content_type

         if DJANGO_TYPE == 'image/jpeg':
             PIL_TYPE = 'jpeg'
             FILE_EXTENSION = 'jpg'
         elif DJANGO_TYPE == 'image/png':
             PIL_TYPE = 'png'
             FILE_EXTENSION = 'png'

         # Open original photo which we want to thumbnail using PIL's Image

         print (self.image.path)
         image = Image.open(self.image)
         image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

         temp_handle = self.image.path
         image.save(temp_handle, PIL_TYPE)

         from django.core.files import File
         reopen = open(temp_handle, "rb")
         django_file = File(reopen)
         
         self.thumbnail.save(temp_handle,django_file, save=False)


    def save(self):
         self.create_thumbnail()
         super(Photo, self).save()


