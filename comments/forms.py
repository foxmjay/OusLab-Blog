from django import forms
from django.forms import ModelForm
from .models import Comment
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class CommentForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['username', 'email', 'message']

    def clean(self):
        super(CommentForm, self).clean()

        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        message = self.cleaned_data.get('message')

        if len(username) < 4:
            self._errors['username'] = self.error_class(['Minimum 4 characters required'])

        if len(message) < 2:
            self._errors['message'] = self.error_class(['Minimum 4 characters required'])

        return self.cleaned_data
