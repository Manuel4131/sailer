fom django.db import models

# Create your models here.
class Store(models.Model):
	name= models.CharField(max_length=30)
	address= models.CharField(max_length=100)
	notes = models.TextField(blank=True, default='')	
	
	def __str__(self):
		return self.name
		

class client(models.Model):
	store=models.ForeignKey('Store', related_name="client") # client: <----
	firstName= models.CharField(max_length= 10) 
	lastName= models.CharField(max_length= 10)
	age= models.IntegerField()
	
	# def __str__(self):
	# 	return self.name
