from django.db import models
from django.conf import settings


class Location(models.Model):
    country = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    locality = models.CharField(max_length=255, null=True)


class Observer(models.Model):
    class Meta:
        unique_together = ('last_name', 'first_name')

    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    is_bander = models.BooleanField(default=False)


class Plover(models.Model):
    class Meta:
        unique_together = ('metal_ring', 'code', 'color')

    bander = models.ForeignKey(Observer, related_name='plovers')
    location = models.ForeignKey(Location, related_name='plovers')
    banding_year = models.IntegerField()
    metal_ring = models.CharField(max_length=20, unique=True)
    code = models.IntegerField()
    color = models.CharField(choices=settings.COLOR_CHOICES, max_length=20)
    sex = models.CharField(choices=settings.SEX_CHOICES, max_length=20)
    age = models.CharField(max_length=5)
    banding_date = models.DateField()
    banding_time = models.TimeField(blank=True)


class Observation(models.Model):
    class Meta:
        ordering = ['-date']

    observer = models.ForeignKey(Observer, related_name='observations')
    plover = models.ForeignKey(Plover, related_name='observations')
    location = models.ForeignKey(Location, related_name='observations')
    date = models.DateField()
    supposed_sex = models.CharField(choices=settings.SEX_CHOICES,
                                    max_length=20)
    coordinate_x = models.FloatField(null=True)
    coordinate_y = models.FloatField(null=True)
    comment = models.TextField(null=True)
