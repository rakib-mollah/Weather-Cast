from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    user = models.ManyToManyField(User, default=None,)
    name = models.CharField(max_length=255, verbose_name="City Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = 'Cities'
