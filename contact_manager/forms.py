from django import forms
from contact_manager.models import Subscriber


class SubscribeForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-input',
            'placeholder': 'Email:'
        }
    ))
    topic = forms.Field(widget=forms.TextInput(attrs={
        'class': 'form-control form-input',
        'placeholder': 'Asunto: '
    }))
    message = forms.Field(widget=forms.Textarea(attrs={
        'class': 'form-control form-input',
        'placeholder': 'Mensaje: '
    }))
