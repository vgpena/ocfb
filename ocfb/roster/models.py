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
	grad_year = models.IntegerField(max_length=4)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	weapon = models.CharField(max_length=1, choices=WEAPON_CHOICES)