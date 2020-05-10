from django import forms
from website.models import COLOR_CHOICES
from django.utils.translation import ugettext_lazy as _
from website.utils.forms_snippets import (
    charfield_template, choicefield_template, emailfield_template,
    coordinatefield_template)


CODE = forms.IntegerField(
    label=_('Code'),
    widget=forms.TextInput(attrs={
        'placeholder': _('Code'),
        'class': 'form-control'
    })
)


class CodeForm(forms.Form):
    code = CODE
    color = choicefield_template(_('Color'), COLOR_CHOICES)


class MetalForm(forms.Form):
    metal_ring = charfield_template(_('Metal ring'), 10, _('Metal ring'))


class MapForm(forms.Form):
    date = forms.DateField(
        label=_('Date'),
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    last_name = charfield_template(_('Last name'), 255, _('Last name'))
    first_name = charfield_template(_('First name'), 255, _('First name'))
    email = emailfield_template(_('Email'), 255, _('Email'))
    town = charfield_template(_('Town'), 255, _('Town'))
    department = charfield_template(_('Department'), 255, _('Department'))
    country = charfield_template(_('Country'), 255, _('Country'))
    locality = charfield_template(_('Locality'), 255, _('Locality'), False)

    coordinate_x = coordinatefield_template(
        _('X coordinate'), _('X coordinate'))
    coordinate_y = coordinatefield_template(
        _('Y coordinate'), _('Y coordinate'))
