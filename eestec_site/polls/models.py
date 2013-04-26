from django.db import models

# Create your models here.
class Publisher(models.Model):
	name = models.CharField(max_length=100)

class Published(models.Model):
	publisher = models.ForeignKey(Publisher)
	year = models.IntegerField()
	value = models.CharField(max_length=100)

class Entry(models.Model):
	format_type = models.CharField(max_length=100)
	language = models.CharField(max_length=100)
	identif = models.CharField(max_length=100)
	file_type = models.CharField(max_length=100)
	short_desc = models.TextField()
	platform =  models.URLField()
	platformName = models.CharField(max_length=100)
	descr = models.TextField()
	author = models.CharField(max_length=100)
	file_name = models.CharField(max_length=100)
	isbn_type = models.CharField(max_length=100)
	isbn_value  = models.CharField(max_length=100)
	body = models.TextField()
	audience = models.CharField(max_length=100)
	
