from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics/')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		super().save()

		img = Image.open(self.image.path)
		c1=0
		c2=0
		c3=img.width
		c4=img.height

		if c4>c3:
			d =(c4 -c3)/2
			c2 = d
			c4 = c4 - d
		else:
			d =(c3 -c4)/2
			c1 = d
			c3 = c3 - d

		if img.height > 300 or img.width > 300:
			img = img.crop((c1,c2,c3,c4))
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)