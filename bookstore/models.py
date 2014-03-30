from django.db import models


CITY_CHOICES =(
	('D', 'Domestic'),
	('I','Import'),
)

class book(models.Model):
	name = models.CharField(max_length = 50)
	#slug = models.SlugField(unique = True)
	author = models.ForeignKey('author')
	publisher = models.ForeignKey('publisher')

	def __unicode__ (self):
		return self.name


class author(models.Model):
	first_name = models.CharField(max_length = 20)
	#slug = models.SlugField(unique = True)
	last_name = models.CharField(max_length = 20)
	#email = models.EmailField() 

	def __unicode__ (self):
		return self.first_name





class publisher(models.Model):
	name = models.CharField(max_length = 30)
	#slug = models.SlugField(unique = True)
	locality = models.CharField(max_length = 1, choices = CITY_CHOICES)

	def __unicode__ (self):
		return self.name
