from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
	"""docstring for Picture"""
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='places')
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1000, blank=True)
	photo = models.ImageField(upload_to='photos', blank=True)
	by = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.title