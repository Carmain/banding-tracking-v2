from django.db import models
from django.conf import settings


class Location(models.Model):
    def __str__(self):
        pattern = '{} - {}, {} ({})'
        return pattern.format(self.town, self.locality,
                              self.department, self.country)

    @property
    def minimal_location(self):
        return '{} ({})'.format(self.town, self.country)

    country = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    locality = models.CharField(max_length=255, null=True)


class Observer(models.Model):
    def __str__(self):
        return self.full_name

    class Meta:
        unique_together = ('last_name', 'first_name')

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    is_bander = models.BooleanField(default=False)


class Plover(models.Model):
    def __str__(self):
        # FIXME: It seem that the get_color_display() doesn't work
        for choice in settings.COLOR_CHOICES:
            if choice[0] == int(self.color):
                color = choice[1]

        return '{} {} ({})'.format(self.code, color, self.metal_ring)

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
    def __str__(self):
        patern = '{} {} : {} - {}'
        return patern.format(self.date, self.observer, self.plover,
                             self.location)

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
