from django.db import models

# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=1200)

	def __str__(self):
		return self.name