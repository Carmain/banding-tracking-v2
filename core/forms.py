from django import forms
from core.models import SEX_CHOICES, COLOR_CHOICES
from django.utils.translation import ugettext_lazy as _


def format_charfield(label, max_length, placeholder, required=True):
    return forms.CharField(
        label=label,
        required=required,
        max_length=max_length,
        widget=forms.TextInput(attrs={
            'placeholder': placeholder,
            'class': 'form-control'
        })
    )


def format_coordinatefield(label, placeholder):
    return forms.FloatField(
        label=label,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': placeholder,
            'readonly': True,
            'class': 'form-control'
        })
    )


def format_choicefield(label, choices):
    return forms.ChoiceField(
        label=label,
        choices=choices,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )


CODE = forms.IntegerField(
    label=_('Code'),
    widget=forms.TextInput(attrs={
        'placeholder': _('Code'),
        'class': 'form-control'
    })
)


class PloverForm(forms.Form):
    code = CODE
    color = format_choicefield(_('Color'), COLOR_CHOICES)
    sex = format_choicefield(_('Sex'), SEX_CHOICES)

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

    last_name = format_charfield(_('Last name'), 255, _('Last name'))
    first_name = format_charfield(_('First name'), 255, _('First name'))
    town = format_charfield(_('Town'), 255, _('Town'))
    department = format_charfield(_('Department'), 255, _('Department'))
    country = format_charfield(_('Country'), 255, _('Country'))
    locality = format_charfield(_('Locality'), 255, _('Locality'), False)

    coordinate_x = format_coordinatefield(_('X coordinate'), _('X coordinate'))
    coordinate_y = format_coordinatefield(_('Y coordinate'), _('Y coordinate'))


class CodeForm(forms.Form):
    code = CODE
    color = format_choicefield(_('Color'), COLOR_CHOICES)


class MetalForm(forms.Form):
    metal_ring = format_charfield(_('Metal ring'), 10, _('Metal ring'))


# Extra forms for the admin section

class ImportPloversForm(forms.Form):
    file = forms.FileField(label=_('File'))
