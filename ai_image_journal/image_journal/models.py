from django.db import models

# Create your models here.

class GeneratedImage(models.Model):
    content = models.TextField() #for prompt content
    image = models.ImageField(upload_to='generated_images') # Path for storing images
    created_at = models.DateTimeField(auto_now_add=True)
