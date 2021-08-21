from django import forms
from .models import *

class NewNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        