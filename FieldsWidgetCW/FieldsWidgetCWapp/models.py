from django.db import models


# Create your models here.

class HeroModel(models.Model):
    name = models.CharField(max_length=50)
    where = models.CharField(max_length=50)
    richOrwhat = models.CharField(max_length=50)
    powers = models.CharField(max_length=50)
    affiliation = models.CharField(max_length=50)
    ability_examples = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
