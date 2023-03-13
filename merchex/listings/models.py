from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    def __str__(self):
        return self.category

    category = models.CharField(max_length=30)


class Band(models.Model):
    def __str__(self):
        return self.name
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MaxValueValidator(2023), MinValueValidator(1900)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    slug = models.SlugField(default="", null=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

class Resources(models.Model):
    def __str__(self):
        return self.title
    
    title = models.fields.CharField(max_length=100)
    link = models.fields.URLField(null=True, blank=True)
