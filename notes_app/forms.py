from django import forms
from django.forms import Textarea
from .models import *

class NewNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'content': Textarea(attrs={'cols': 100, 'rows': 20}),
        }