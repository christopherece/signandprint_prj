from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Service(models.Model):

    TYPE_CHOICES = [
        ('signage', 'Signage'),
        ('display_signs', 'Display Signs'),
        ('digital_printing', 'Digital Printing'),
        ('vehicle_signs', 'Vehicle Signs'),
    ]
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True)
    image = models.ImageField(upload_to='services/')
    size = models.CharField(max_length=50, blank=True, null=True)
    price_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    usage = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='signage')
    def __str__(self):
        return self.name
