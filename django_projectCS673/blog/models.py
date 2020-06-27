from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# What we want to save to the database

#This can help create SQL commands for our table
class Post(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField() #Unrestricted lines and lines of words
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)  #one-to-many relationship one user can have many posts but not other way
	#on_delete - if User deleted, post deleted
	def __str__(self):
		return self.title #how we want post to be printed out, just the title
		
	#not using redirect, reverse will return full url as string
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})


allergy_choices = (
	(1, 'Nuts'),
	(2, 'Seafood'),
	(3, 'Shellfish'),
	(4, 'Egg'),
	(5, 'Dairy'),
	(6, 'Wheat'),
	(7, 'Soy'),
)

class Menu(models.Model):
	restaurant = models.CharField(max_length = 100, unique=True, primary_key = True)
	description = models.TextField() #Unrestricted lines and lines of words
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)  #one-to-many relationship one user can have many posts but not other way
	#on_delete - if User deleted, post deleted
	def __str__(self):
		return self.restaurant #how we want post to be printed out, just the title
		
	#not using redirect, reverse will return full url as string
	def get_absolute_url(self):
		return reverse('menu-detail', kwargs={'pk': self.pk}) #NEED TO CHANGE 'post-detail' link to a new 'Menu-Link' which effectively be the website...