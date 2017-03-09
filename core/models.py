from django.db import models
from django.utils.translation import ugettext_lazy as _

SEX_CHOICES = (
    ('M', _('Male')),
    ('F', _('Female')),
    ('U', _('Undetermined'))
)

COLOR_CHOICES = (
    ('R', _('Red')),
    ('W', _('White')),
    ('Y', _('Yellow')),
    ('G', _('Green'))
)


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
        return '{} {} ({})'.format(self.code, self.get_color_display(),
                                   self.metal_ring)

    class Meta:
        unique_together = ('metal_ring', 'code', 'color')

    bander = models.ForeignKey(Observer, related_name='plovers',
                               on_delete=models.PROTECT)
    location = models.ForeignKey(Location, related_name='plovers',
                                 on_delete=models.PROTECT)
    banding_year = models.IntegerField()
    metal_ring = models.CharField(max_length=20, unique=True)
    code = models.IntegerField()
    color = models.CharField(choices=COLOR_CHOICES, max_length=20, default=0)
    sex = models.CharField(choices=SEX_CHOICES, max_length=20, default=2)
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

    observer = models.ForeignKey(Observer, related_name='observations',
                                 null=True, on_delete=models.SET_NULL)
    plover = models.ForeignKey(Plover, related_name='observations',
                               on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='observations',
                                 on_delete=models.CASCADE)
    date = models.DateField()
    supposed_sex = models.CharField(choices=SEX_CHOICES,
                                    max_length=20, default=2)
    coordinate_x = models.FloatField(null=True)
    coordinate_y = models.FloatField(null=True)
    comment = models.TextField(null=True)
