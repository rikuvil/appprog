from django import forms

from .models import *

class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['name', 'genre', 'available', 'max_players', 'play_time']
        labels = {'name': 'Title', 
                  'genre': 'Genre', 
                  'available': 'Available',
                  'max_players': 'Maximum amount of players',
                  'play_time': 'Estimated playtime in hours'}
        
class BoardGameReviewForm(forms.ModelForm):
    class Meta:
        model = BoardGameReview
        fields = ['review', 'stars', 'favourite']
        labels = {'review': 'Review',
                  'stars': 'Stars',
                  'favourite': 'Favourite'}