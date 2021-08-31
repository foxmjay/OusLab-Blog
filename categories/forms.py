from django import forms
from django.forms import ModelForm
from .models import Categorie
from django.core.exceptions import ValidationError


class CategorieForm(ModelForm):

    class Meta:
        model = Categorie
        fields = ['name']

    def clean(self):
        super(CategorieForm, self).clean()
        title = self.cleaned_data.get('name')
        if len(title) < 2:
            self._errors['name'] = self.error_class(['Minimum 2 characters required'])
        return self.cleaned_data
