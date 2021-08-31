from django import forms
from django.forms import ModelForm
from .models import Library
from django.core.exceptions import ValidationError


class LibraryForm(ModelForm):

    class Meta:
        model = Library
        fields = ['path']