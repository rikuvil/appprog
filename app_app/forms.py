from django import forms

from .models import *

class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['name', 'genre', 'available']
        labels = {'name': 'Title', 
                  'genre': 'Genre', 
                  'available': 'Available'}
        
class BoardGameReviewForm(forms.ModelForm):
    class Meta:
        model = BoardGameReview
        fields = ['review', 'stars', 'favourite']
        labels = {'review': 'Review',
                  'stars': 'Stars',
                  'favourite': 'Favourite'}