from django.db import models

# Create your models here.

class Contact(models.Model):
    SERVICE_TYPE_CHOICES = [
            ('signage', 'Signage'),
            ('display_signs', 'Display Signs'),
            ('digital_printing', 'Digital Printing'),
            ('vehicle_signs', 'Vehicle Signs'),

        ]
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=150, blank=True, null=True)
    phone = models.IntegerField(max_length=50, blank=True, null=True)
    subject = models.TextField()
    category = models.CharField(
        max_length=150,
        choices=SERVICE_TYPE_CHOICES,
        default='Please select Service',
        )
    description = models.TextField()

    def __str__(self):
            return self.name