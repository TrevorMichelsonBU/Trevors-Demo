from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) #user associated with 1 Profile
	image = models.ImageField(default='default.jpg', upload_to='profile-pics') #profile-pics is directory pic will be uploaded to, default set

	def __str__(self):
		return f'{self.user.username} Profile' #prints this out instead of just some default words
		
	def save(self,*args, **kwargs): #overriding save
		super().save(*args, **kwargs) #runs parent class save function
		
		#Resets image uploaded if too large
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

