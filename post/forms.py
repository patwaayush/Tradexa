from django import forms
from .models import Post
from django.core import validators


class PostForm(forms.Form):
    text_field = forms.CharField(max_length=2000,widget=forms.Textarea, label='Content',
    validators = [validators.MinLengthValidator(10)])