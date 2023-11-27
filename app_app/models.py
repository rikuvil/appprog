from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default='none')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_games')
    available = models.BooleanField(default=True)
    loaned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='loaned_games')

    date_added = models.DateTimeField(default=timezone.now)
    #last_modified = models.DateTimeField(default=timezone.now)
    # Add other fields as needed

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Board game'

class BoardGamer(models.Model):
    name = models.CharField(max_length=100)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #borrowed_games = models.ManyToManyField(BoardGame, through='GameLoan')
    # Add other fields as needed

    def __str__(self):
        return self.name
    

class BoardGameReview(models.Model):
    review = models.TextField()
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    favourite = models.BooleanField(default=False)

    # Times
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # Game
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.review} by {self.owner}'


class GameLoan(models.Model):
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    #borrower = models.ForeignKey(BoardGamer, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.board_game} - {self.borrower} - {self.loan_date}"
    
    #Display the most recent loan first
    class Meta:
        ordering = ['-loan_date']
