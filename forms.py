
from django import forms
from .models import Ressource


class RessourceForm(forms.ModelForm):

    class Meta:
        model = Ressource

        fields = [
            'titre',
            'description',
            'type',
            'url',
            'categorie',
        ]

        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre de la ressource'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description de la ressource',
                'rows': 4
            }),

            'type': forms.Select(attrs={
                'class': 'form-control'
            }),

            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com'
            }),

            'categorie': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
