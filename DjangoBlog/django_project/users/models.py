from django.db import models
from django.contrib.auth.models import User
from PIL  import Image

# Create your models here.
class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg', upload_to='profile_pics')


	def __str__(self):
		return '{} Profile'.format(self.user.username)

# https://stackoverflow.com/questions/54084710/syntaxerror-invalid-syntax-for-collectstatic-python
# You are trying to use f-string in Python 3.5 but they appeared in Python 3.6.
# Change f'{self.user.username} Profile' to be '{} Profile'.format(self.user.username) or change your Python to be 3.6.		

	def save(self, *args, **kawrgs):
		super().save()

		img=Image.open(self.image.path)

		if (img.height>300 or img.width>300):
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)