from django.db.models.signals import post_save #want to save after user created
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User) #when a user is saved, send the post_save signal to the create_profile function
def create_profile(sender, instance, created, **kwargs):
	if created: #if user is created
		Profile.objects.create(user=instance) #user will be made with instance

@receiver(post_save, sender=User) #when a user is saved, send the post_save signal to the create_profile function
def save_profile(sender, instance, **kwargs):
	instance.profile.save()


