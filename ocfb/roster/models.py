from django.db import models


"""
Options for gender (until collegiate fencing becomes more progressive) and weapon.

"""
GENDER_CHOICES = (
	('F', 'Female'),
	('M', 'Male'),
)

WEAPON_CHOICES = (
	('E', 'Epee'),
	('F', 'Foil'),
	('S', 'Sabre'),
)


class Member(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=40)
	slug = models.SlugField(max_length=40)
	grad_year = models.IntegerField(max_length=4, blank=True, null=True)
	titles = models.CharField(max_length=250, blank=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	weapon = models.CharField(max_length=1, choices=WEAPON_CHOICES)
	photo = models.ForeignKey('daguerre.Image', blank=True, null=True)
	bio = models.TextField()
	
	def __unicode__(self):
		return (self.slug)