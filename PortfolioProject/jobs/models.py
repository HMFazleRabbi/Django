from django.db import models

# Django Super user
# h-m-fazle.rabbi@Django123

# Create your models here.
class Job(models.Model):
    # Image
    image = models.ImageField(upload_to='images/')
    # Summary
    summary = models.CharField(max_length=200)
    #Title
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title