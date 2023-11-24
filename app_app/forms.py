from django import forms

from .models import *

class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['name', 'genre']
        labels = {'name': 'Title', 'genre': 'Genre'}