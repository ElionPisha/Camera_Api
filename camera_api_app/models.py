from django.db import models

# Create your models here.
class Camera(models.Model):
    series = models.IntegerField()
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.name
