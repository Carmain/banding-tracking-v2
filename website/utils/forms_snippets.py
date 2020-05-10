from django import forms


def charfield_template(label, max_length, placeholder, required=True):
    return forms.CharField(
        label=label,
        required=required,
        max_length=max_length,
        widget=forms.TextInput(attrs={
            'placeholder': placeholder,
            'class': 'form-control'
        })
    )


def choicefield_template(label, choices):
    return forms.ChoiceField(
        label=label,
        choices=choices,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
