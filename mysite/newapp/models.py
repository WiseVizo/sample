from django.db import models

# Create your models here.
class MovieData(models.Model):
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    duration = models.FloatField()

    def __str__(self) -> str:
        return self.name
    
    