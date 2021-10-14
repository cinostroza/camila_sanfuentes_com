from django import forms
from contact_manager.models import Subscriber


class SubscribeForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
