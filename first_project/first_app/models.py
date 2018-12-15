from django.db import models # models is a file name

# Create your models here.
class Topic(models.Model):# model is a class inside a models file.model represents table or 
#collection in our database where every attribute of the class "Topic" is field of the table or collection 
	top_name=models.CharField(max_length=264,unique=True)# charField is another class inside models
											# max_length and unique are constraints or attributes of charfield
											# unique is true coz every topic must be unique to identify easily
	def __str__(self):  # __str__ dunder returns readble string format
		return self.top_name

class webpage(models.Model):
	topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
	name=models.CharField(max_length=264,unique=True)
	url=models.URLField(unique=True)

	def __str__(self):
		return self.name

class AccessRecord(models.Model):
	name=models.ForeignKey(webpage,on_delete=models.CASCADE)
	date=models.DateField()

	def __str__(self):
		return str(self.date)