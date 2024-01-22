from django.db import models

# Create your models here.
class Python_data(models.Model):
    Question = models.TextField()
    Answer = models.TextField()
    Unit = models.DecimalField( max_digits=5, decimal_places=2)