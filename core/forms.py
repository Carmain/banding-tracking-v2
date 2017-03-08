from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


def format_charfield(label, max_length, placeholder, required=True):
    return forms.CharField(
        label=_(label),
        required=required,
        max_length=max_length,
        widget=forms.TextInput(attrs={
            'placeholder': _(placeholder),
            'class': 'form-control'
        })
    )


def format_coordinate_field(label, placeholder):
    return forms.FloatField(
        label=_(label),
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': _(placeholder),
            'class': 'form-control'
        })
    )


def format_choicefield(label, choices):
    return forms.ChoiceField(
        label=_(label),
        choices=choices,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )


code = forms.IntegerField(
    label=_('Code'),
    widget=forms.TextInput(attrs={
        'placeholder': _('Code'),
        'class': 'form-control'
    })
)


class PloverForm(forms.Form):
    code = code
    color = format_choicefield('Color', settings.COLOR_CHOICES)
    sex = format_choicefield('Sex', settings.SEX_CHOICES)

    comment = forms.CharField(
        label=_('Comment'),
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3
        })
    )


class MapForm(forms.Form):
    date = forms.DateField(
        label=_('Date'),
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    last_name = format_charfield('Last name', 255, 'Last name')
    first_name = format_charfield('First name', 255, 'First name')
    town = format_charfield('Town', 255, 'Town')
    department = format_charfield('Department', 255, 'Department')
    country = format_charfield('Country', 255, 'Country')
    location = format_charfield('Location', 255, 'Location', False)

    coordinate_x = format_coordinate_field('X coordinate', 'X coordinate')
    coordinate_y = format_coordinate_field('X coordinate', 'X coordinate')


class CodeForm(forms.Form):
    code = code
    color = format_choicefield('Color', settings.COLOR_CHOICES)


class MetalForm(forms.Form):
    metal_ring = format_charfield('Metal ring', 10, 'Metal ring')
