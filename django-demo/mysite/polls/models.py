from django.db import models

# Create your models here.
class Person(models.Model):
    first_name  = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)