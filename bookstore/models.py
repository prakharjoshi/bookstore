from django.db import models

CHOICES = (
	('D', 'Domestic'),
	('I','Import'),
)

class book(models.Model):
	name = models.CharField(max_length = 50)
    	author = models.ForeignKey('author')
	publisher = models.ForeignKey('publisher')  

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


class signup(models.Model):
	username = models.CharField(max_length = 50)
	


	def __unicode__ (self):
		return self.username
	

class sign(models.Model):
	username = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.username


class User(models.Model):
	username = models.CharField(max_length = 30)
	password = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.username



