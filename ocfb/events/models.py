from django.db import models
from gallery.models import Photo, Gallery
from daguerre.models import Image

class Category(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)
	
	class Meta:
		verbose_name_plural = 'categories'
	
	
	def __unicode__(self):
		return (self.slug)

class Event(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=200)
	category = models.ForeignKey('Category', blank=True, null=True)
	link = models.URLField()
	location = models.CharField(max_length=250)
	date = models.DateTimeField()
	summary = models.TextField(blank=True)
	preview_image = models.ForeignKey('daguerre.Image', blank=True, null=True)
	media_gallery = models.ForeignKey('gallery.Gallery', blank=True, null=True)
	
	def __unicode__(self):
		return (self.slug)