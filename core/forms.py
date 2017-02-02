from django import forms
from django.utils.translation import ugettext_lazy as _


class PloverForm(forms.Form):
    COLOR_CHOICES = (
        (1, _("Red")),
        (2, _("White")),
        (3, _("Yellow")),
        (4, _("Green"))
    )

    SEX_CHOICES = (
        (1, _("Male")),
        (2, _("Female")),
        (3, _("Undetermined"))
    )

    code = forms.IntegerField(
        label=_('Code'),
        widget=forms.TextInput(attrs={
            'placeholder': _('Code'),
            'class': 'form-control'
        })
    )

    color = forms.ChoiceField(
        label=_('Color'),
        choices=COLOR_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    sex = forms.ChoiceField(
        label=_('Sex'),
        choices=SEX_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    comment = forms.CharField(
        label=_('Comment'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3
        })
    )


class MapForm(forms.Form):
    date = forms.DateField(
        label=_('Date'),
        widget=forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    last_name = forms.CharField(
        label=_('Last name'),
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': _('Last name'),
            'class': 'form-control'
        })
    )

    first_name = forms.CharField(
        label=_('First name'),
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': _('First name'),
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
