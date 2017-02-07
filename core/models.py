from django.db import models
from django.utils.translation import ugettext_lazy as _


class Location(models.Model):
    town = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    locality = models.CharField(max_length=255, blank=True)


class Observer(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    is_bander = models.BooleanField(default=False)


# Useless fileds ?
# `year` int(11) DEFAULT NULL,
# `action` varchar(6) DEFAULT NULL,
# `date` varchar(10) DEFAULT NULL,
class Plover(models.Model):
    COLORS = (
        (1, _("Red")),
        (2, _("White")),
        (3, _("Yellow")),
        (4, _("Green"))
    )

    SEX = (
        (1, _("Male")),
        (2, _("Female")),
        (3, _("Undetermined"))
    )

    bander = models.ForeignKey(Observer, related_name='plovers', default=None)
    location = models.ForeignKey(Location, related_name='plovers', default=None)
    banding_year = models.IntegerField()
    metal_ring = models.CharField(max_length=20, unique=True)
    code = models.IntegerField()
    color = models.CharField(choices=COLORS, max_length=20)
    sex = models.CharField(choices=SEX, max_length=20)
    age = models.CharField(max_length=5)
    banding_date = models.DateField()
    banding_time = models.TimeField(blank=True)


class Observation(models.Model):
    observer = models.ForeignKey(Observer, related_name='observations')
    plover = models.ForeignKey(Plover, related_name='observations')
    location = models.ForeignKey(Location, related_name='observations')
    date = models.DateField()
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
    comment = models.TextField()
