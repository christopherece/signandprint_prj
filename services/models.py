from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Service(models.Model):

    name = models.CharField(max_length=100)
    description = RichTextField(blank=True)
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.name
    
class Item(models.Model):
    service = models.ForeignKey(Service, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True)
    
    # Price is now just a simple CharField
    price = models.CharField(max_length=100)  # No min/max length, just a string
    
    image = models.ImageField(upload_to='items/')
    
    def __str__(self):
        return self.name