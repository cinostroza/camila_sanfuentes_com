from django import forms
from .models import Post
from django.utils import timezone


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'post_header_image')
        today = timezone.now()
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass', 'id': 'testID'}),
        }
