from django import template
from django.conf import settings


register = template.Library()


@register.filter
def sex_to_string(value):
    for choice in settings.SEX_CHOICES:
        if choice[0] == int(value):
            return choice[1]

    return None


@register.filter
def color_to_string(value):
    for choice in settings.COLOR_CHOICES:
        if choice[0] == int(value):
            return choice[1]

    return None
