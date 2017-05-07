from django import forms
from core.models import SEX_CHOICES, COLOR_CHOICES
from django.utils.translation import ugettext_lazy as _
from extras.forms_snippets import charfield_template, coordinatefield_template
from extras.forms_snippets import choicefield_template, emailfield_template


CODE = forms.IntegerField(
    label=_('Code'),
    widget=forms.TextInput(attrs={
        'placeholder': _('Code'),
        'class': 'form-control'
    })
)


class PloverForm(forms.Form):
    code = CODE
    color = choicefield_template(_('Color'), COLOR_CHOICES)
    sex = choicefield_template(_('Sex'), SEX_CHOICES)

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


class CodeForm(forms.Form):
    code = CODE
    color = choicefield_template(_('Color'), COLOR_CHOICES)


class MetalForm(forms.Form):
    metal_ring = charfield_template(_('Metal ring'), 10, _('Metal ring'))


# Extra forms for the admin section

class ImportPloversForm(forms.Form):
    file = forms.FileField(label=_('File'))
