from django.db import models
from django.contrib.auth.models import User
from mysite.settings.base import MEDIA_ROOT
from time import time

CHOICES = (
	('D', 'Domestic'),
	('I','Import'),
)


def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)

class book(models.Model):
	name = models.CharField(max_length = 50)
    	author = models.ForeignKey('author')
	publisher = models.ForeignKey('publisher')
	category = models.CharField(max_length = 20)
	docfile = models.FileField(upload_to = get_upload_file_name)

	def __unicode__(self):
		return self.name

class author(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	

	def __unicode__(self):
		return self.first_name + self.last_name

	

class publisher(models.Model):
	name = models.CharField(max_length = 30)
	locality = models.CharField(max_length = 1, choices = CHOICES)

	def __unicode__(self):
		return self.name




