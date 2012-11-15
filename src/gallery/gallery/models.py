from django.db import models

"""
I want to put videos here eventually, but photos will do fine for now.
Might want to use https://github.com/andrewebdev/django-video for that?

"""



class Gallery(models.Model):
	"""
	Also needs (as an optional field) a FK to an Event from another yet-to-be-made app.
	
	"""
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200)
	slug = models.SlugField(max_length=100)
	index = models.PositiveIntegerField(help_text="This can be used to determine the order in which the galleries are displayed.")
	
	class Meta:
		verbose_name_plural = 'galleries'
		
	def __unicode__(self):
		return (self.title)
	
	
class Photo(models.Model):
	image = models.ForeignKey('daguerre.image')
	credit = models.CharField(max_length=200, blank=True)
	caption = models.CharField(max_length=300, blank=True)
	gallery = models.ForeignKey('Gallery', related_name="photos")
	slug = models.SlugField(max_length=200)
	
	def __unicode__(self):
		return(self.slug)