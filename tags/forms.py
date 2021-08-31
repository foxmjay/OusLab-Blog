from django import forms
from django.forms import ModelForm
from .models import Tag
from django.core.exceptions import ValidationError


class TagForm(ModelForm):

    class Meta:
        model = Tag
        fields = ['name']

    def clean(self):
        super(TagForm, self).clean()

        title = self.cleaned_data.get('name')

        if len(title) < 2:
            self._errors['name'] = self.error_class(['Minimum 2 characters required'])

        return self.cleaned_data
