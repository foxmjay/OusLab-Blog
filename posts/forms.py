from django import forms
from django.forms import ModelForm
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'front_image',
                  'content_image',
                  'description',
                  'content',
                  'post_type',
                  'published',
                  'published_at',
                  'fb_comment_url']

    def clean(self):
        super(PostForm, self).clean()

        title = self.cleaned_data.get('title')

        if len(title) < 4:
            self._errors['title'] = self.error_class(['Minimum 4 characters required'])

        return self.cleaned_data
