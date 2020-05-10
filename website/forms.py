from django import forms
from website.models import COLOR_CHOICES
from django.utils.translation import ugettext_lazy as _
from website.utils.forms_snippets import charfield_template
from website.utils.forms_snippets import choicefield_template


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
