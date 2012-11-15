from django.db import models

from daguerre.models import Image


"""
Options for gender (until collegiate fencing becomes more progressive) and weapon.

"""
GENDER_CHOICES = (
	('Women\'s', 'Female'),
	('Men\'s', 'Male'),
)

WEAPON_CHOICES = (
	('Epee', 'Epee'),
	('Foil', 'Foil'),
	('Sabre', 'Sabre'),
)


class Member(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=40)
	slug = models.SlugField(max_length=40)
	current_member = models.BooleanField()
	grad_year = models.IntegerField(max_length=4, blank=True, null=True)
	titles = models.CharField(max_length=250, blank=True)
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	weapon = models.CharField(max_length=10, choices=WEAPON_CHOICES)
	photo = models.ForeignKey('daguerre.Image', blank=True, null=True)
	bio = models.TextField()
	
	def __unicode__(self):
		return (self.slug)