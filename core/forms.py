from django import forms
from django.utils.translation import ugettext_lazy as _


class MapForm(forms.Form):
    date = forms.DateField(
        label=_('Date'),
        widget=forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    town = forms.CharField(
        label=_('Town'),
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': _('Town'),
            'class': 'form-control'
        })
    )

    department = forms.CharField(
        label=_('Department'),
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': _('Department'),
            'class': 'form-control'
        })
    )

    country = forms.CharField(
        label=_('Country'),
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': _('Country'),
            'class': 'form-control'
        })
    )

    location = forms.CharField(
        label=_('Location'),
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': _('Location'),
            'class': 'form-control'
        })
    )

    coordinate_x = forms.FloatField(
        label=_('X coordinate'),
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': _('X coordinate'),
            'class': 'form-control'
        })
    )

    coordinate_y = forms.FloatField(
        label=_('Y coordinate'),
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': _('Y coordinate'),
            'class': 'form-control'
        })
    )
